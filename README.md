# AI Team Ops Template

작은 팀이 AI 에이전트를 **챗봇이 아니라 팀원처럼 운영**하기 위한 공개 템플릿입니다.

KDA4 공유용으로 먼저 만든 public-safe 샘플입니다. 실제 개인 메모, 채팅 ID, 토큰, 내부 프로젝트 정보는 포함하지 않고, 모두 가짜 예시 데이터로 구성했습니다.

## 무엇을 해결하나요?

AI 에이전트를 여러 개 쓰기 시작하면 보통 이런 문제가 생깁니다.

- 누가 무엇을 맡았는지 흐려짐
- 채팅, GitHub, 노트, 작업 로그가 흩어짐
- 에이전트 답변을 검증하지 않고 바로 믿게 됨
- 한 번 만든 운영 방식이 다음 프로젝트로 재사용되지 않음

이 템플릿은 다음 흐름을 제공합니다.

1. 메시지 채널에서 작업 요청
2. GitHub Issue로 작업 단위 정리
3. 에이전트 역할과 handoff 양식으로 위임
4. Obsidian식 지식 폴더에 결정/학습 저장
5. PR/리뷰/일일 브리프로 검증

## 10분 Quickstart

```sh
git clone https://github.com/YOUR_ID/ai-team-ops-template.git
cd ai-team-ops-template
cp .env.example .env
./scripts/setup-demo.sh
./scripts/validate-config.sh
```

실제 API 키 없이도 demo mode로 구조를 볼 수 있습니다.

## Repo 구조

```text
docs/        개념, 아키텍처, KDA4 워크숍 문서
examples/    가짜 팀/이슈/노트/채널 예시
templates/   에이전트 역할, handoff, issue, PR, brief 템플릿
scripts/     데모 설치, 검증, 비밀정보 스캔
plugins/     public-safe 예시 플러그인 자리
```

## 핵심 원칙

- 좋은 샘플은 숨기는 게 아니라 fork할 수 있게 공개한다.
- 운영 방식은 프롬프트보다 중요하다.
- 에이전트 작업은 반드시 상태 파일, 근거, 검증 결과를 남긴다.
- 공개 repo에는 실제 개인정보/토큰/채팅 ID를 절대 넣지 않는다.

## KDA4에서 써보는 방법

1. Fork
2. `examples/demo-agency`를 자기 팀/프로젝트 이름으로 수정
3. `templates/agent-role.md`로 역할 정의
4. `templates/handoff.md`로 작업 요청
5. GitHub Issue와 PR에 연결

자세한 안내: [docs/kda4-workshop.md](docs/kda4-workshop.md)

## License

- Code: MIT
- Docs/templates: CC BY 4.0 취지로 자유롭게 복사/수정 가능. 정확한 법적 분리는 추후 필요하면 보강하세요.
