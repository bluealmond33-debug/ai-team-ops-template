#!/usr/bin/env bash
set -euo pipefail

mkdir -p examples/sample-obsidian-vault/{00\ Inbox,01\ Projects,02\ Decisions,03\ Learnings,04\ Worklogs}

if [ ! -f .env ]; then
  cp .env.example .env
  echo "Created .env from .env.example"
fi

echo "Demo workspace ready. Next: ./scripts/validate-config.sh"
