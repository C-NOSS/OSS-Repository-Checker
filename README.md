# OSS Repository Check

`oss-repo-check`는 오픈소스 프로젝트에 처음 참여하는 사람이 저장소의 기본 기여 환경을 빠르게 확인할 수 있도록 만든 작은 Python CLI 도구입니다.

저장소 URL을 입력하면 다음 항목의 존재 여부를 확인합니다.

- README
- CONTRIBUTING 가이드
- Code of Conduct
- License
- Issue Template
- Pull Request Template

## 왜 만들었나요?

처음 오픈소스 프로젝트를 접하면 코드보다 먼저 프로젝트의 기여 규칙과 커뮤니티 문화를 이해해야 한다고 생각합니다. 이 프로젝트는 신규 기여자가 저장소의 온보딩 준비 상태를 빠르게 살펴보고, 어떤 문서를 먼저 읽어야 하는지 구성을 살펴보고 판단하는 데 도움을 주는 것을 목표로 합니다.

## 설치

```bash
python -m pip install -e .
```

## 사용법

```bash
oss-repo-check https://github.com/[repo]
```

또는 owner/repository 형식으로도 실행할 수 있습니다.

```bash
oss-repo-check [owner/repo]
```

## 출력 예시

```text
Repository: owner/repo
README                 OK
CONTRIBUTING            OK
CODE_OF_CONDUCT         OK
LICENSE                 OK
ISSUE_TEMPLATE          OK
PULL_REQUEST_TEMPLATE   MISSING

Score: 5/6
```

## 개발

```bash
python -m pip install -e .[dev]
pytest
```

### AI 활용 안내

본 프로젝트는 코딩과 오픈소스 개발을 처음 접하는 입문자들이 생성형 AI를 활용하여 코드 작성 및 개발 과정을 학습하는 프로젝트입니다.
프로젝트 내 일부 또는 전체 코드는 생성형 AI를 통해 작성되었으며, 참여자들의 학습과 실습을 목적으로 활용하고 있습니다.
이에 따라 코드의 구조, 구현 방식 및 완성도에 부족한 부분이 있을 수 있습니다. 이를 고려한 건설적인 피드백과 개선 의견을 환영합니다.



자세한 기여 절차는 [CONTRIBUTING.md](CONTRIBUTING.md)를 참고하세요.
