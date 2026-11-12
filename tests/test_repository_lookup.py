import sys

import requests

from oss_repo_check import checks, cli


REPOSITORY_URL = "https://api.github.com/repos/example/project"


def mock_github_responses(monkeypatch, responses):
    requested_urls = []

    def fake_get(url, **kwargs):
        requested_urls.append(url)
        response = requests.Response()
        response.status_code = responses[url]
        response.url = url
        return response

    monkeypatch.setattr(checks.requests, "get", fake_get)
    return requested_urls


def test_missing_repository_stops_before_file_checks(monkeypatch, capsys):
    requested_urls = mock_github_responses(monkeypatch, {REPOSITORY_URL: 404})
    monkeypatch.setattr(sys, "argv", ["oss-repo-check", "example/project"])

    assert cli.main() == 1

    captured = capsys.readouterr()
    assert "Repository not found or inaccessible: example/project" in captured.out
    assert "MISSING" not in captured.out
    assert requested_urls == [REPOSITORY_URL]


def test_missing_file_in_existing_repository_is_reported(monkeypatch, capsys):
    readme_url = f"{REPOSITORY_URL}/contents/README.md"
    license_url = f"{REPOSITORY_URL}/contents/LICENSE"

    monkeypatch.setattr(
        checks,
        "CHECKS",
        {"README": ("README.md",), "LICENSE": ("LICENSE",)},
    )
    requested_urls = mock_github_responses(
        monkeypatch,
        {REPOSITORY_URL: 200, readme_url: 404, license_url: 200},
    )
    monkeypatch.setattr(sys, "argv", ["oss-repo-check", "example/project"])

    assert cli.main() == 0

    output_lines = capsys.readouterr().out.splitlines()
    assert f"{'README':<24} MISSING" in output_lines
    assert f"{'LICENSE':<24} OK" in output_lines
    assert requested_urls == [REPOSITORY_URL, readme_url, license_url]
