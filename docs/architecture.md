# Architecture

## 기본 흐름

```text
User request
  -> Messaging channel
  -> GitHub Issue
  -> Agent handoff
  -> Evidence/state file
  -> PR or output
  -> Review
  -> Brief / knowledge note
```

## 구성 요소

- **Messaging**: Telegram, Discord, Slack 등. 빠른 요청과 알림.
- **GitHub**: 작업 단위, 코드 변경, 리뷰, 이력.
- **Obsidian-style vault**: 결정, 회고, 운영 원칙, 프로젝트 지식 저장.
- **Agents**: 역할이 명확한 AI 작업자. 예: builder, reviewer, researcher.
- **State files**: 긴 작업을 채팅 기억에 의존하지 않고 이어가기 위한 짧은 보고서.

## 권장 채널 구조

- `#start`: 사용법과 규칙
- `#requests`: 새 작업 요청
- `#handoffs`: 에이전트 위임/응답
- `#reviews`: 검토와 승인
- `#briefs`: 일일 요약
- `#logs-private`: 공개 repo에는 넣지 않는 내부 로그

## 안전 원칙

- 공개용 repo는 항상 synthetic data만 사용
- `.env`, 토큰, 채팅 ID, 실제 고객/팀 로그 commit 금지
- 에이전트 결과는 근거와 검증을 함께 남김
