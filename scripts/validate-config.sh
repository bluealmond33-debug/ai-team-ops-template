#!/usr/bin/env bash
set -euo pipefail

required=(README.md QUICKSTART.md docs/architecture.md docs/kda4-workshop.md templates/handoff.md examples/demo-agency/team.yaml)

for file in "${required[@]}"; do
  if [ ! -f "$file" ]; then
    echo "Missing required file: $file" >&2
    exit 1
  fi
done

if [ -f .env ] && grep -Eiq '(token|key|secret)=.+[A-Za-z0-9_\-]{12,}' .env; then
  echo "Possible real secret in .env. Do not commit .env." >&2
  exit 1
fi

echo "Validation OK"
