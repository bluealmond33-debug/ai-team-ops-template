# QUICKSTART

## 1. Fork 또는 clone

```sh
git clone https://github.com/YOUR_ID/ai-team-ops-template.git
cd ai-team-ops-template
```

## 2. demo 설정 만들기

```sh
cp .env.example .env
./scripts/setup-demo.sh
```

## 3. 검증

```sh
./scripts/validate-config.sh
python3 scripts/secret_scan.py .
```

## 4. 자기 프로젝트에 맞게 바꾸기

- `examples/demo-agency/team.yaml`: 팀/에이전트 이름 수정
- `examples/sample-discord-layout.md`: 채널 구조 수정
- `templates/agent-role.md`: 에이전트 역할 정의
- `templates/handoff.md`: 작업 위임 양식 수정
- `examples/sample-obsidian-vault`: 결정/학습 저장소로 사용

## 5. 실제 도구 연결 전 체크

- `.env`는 commit 금지
- 실제 토큰은 GitHub Secret 또는 로컬 환경변수 사용
- 채팅방 ID, 개인 노트, 내부 로그는 예시 파일에 넣지 않기
