from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict

import requests

from .checks import check_repository, parse_repo


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="oss-repo-check",
        description="Check whether a GitHub repository exposes common contributor onboarding files.",
    )
    parser.add_argument("repository", help="GitHub URL or owner/repository")
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print check results as JSON.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()

    try:
        owner, repo = parse_repo(args.repository)
        results = check_repository(owner, repo)
    except ValueError as exc:
        print(f"Input error: {exc}", file=sys.stderr if args.json else sys.stdout)
        return 2
    except requests.RequestException as exc:
        print(f"GitHub API error: {exc}", file=sys.stderr if args.json else sys.stdout)
        return 1

    score = sum(result.found for result in results)

    if args.json:
        report = {
            "repository": f"{owner}/{repo}",
            "checks": [asdict(result) for result in results],
            "score": score,
            "total": len(results),
        }
        print(json.dumps(report, indent=2))
        return 0

    print(f"Repository: {owner}/{repo}")
    for result in results:
        status = "OK" if result.found else "MISSING"
        print(f"{result.name:<24} {status}")

    print(f"\nScore: {score}/{len(results)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
