# Handoff Template

```text
[HANDOFF]
TASK: PROJECT-YYYYMMDD-SHORT-01
FROM: <requester>
TO: <agent/reviewer>
PROJECT: <project name>
ORIGIN: <channel or issue link>
REPLY TO: <where the final answer should return>
STATE: <path to state file or issue link>
REQUEST: <one concrete request>
CONSTRAINTS:
- <constraint 1>
- <constraint 2>
EXPECTED OUTPUT:
- STATUS
- CHECKED
- NOT_CHECKED
- BLOCKER
- EVIDENCE
- NEXT
```

## Example

```text
[HANDOFF]
TASK: DEMO-20260606-README-01
FROM: Mingi
TO: Reviewer Agent
PROJECT: demo-ai-team
ORIGIN: GitHub Issue #1
REPLY TO: GitHub Issue #1
STATE: docs/kda4-workshop.md
REQUEST: Review whether this workshop guide is clear for beginners.
CONSTRAINTS:
- Do not rewrite everything.
- Point out confusing steps only.
EXPECTED OUTPUT: STATUS + CHECKED + NOT_CHECKED + BLOCKER + EVIDENCE + NEXT
```
