#!/usr/bin/env python3
import os
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')
SKIP_DIRS = {'.git', 'node_modules', '__pycache__'}
PATTERNS = [
    ('private_token_like', re.compile(r'(?i)(api[_-]?key|token|secret|password)\s*[:=]\s*[A-Za-z0-9_\-]{12,}')),
    ('telegram_chat_id_like', re.compile(r'-100\d{8,}')),
    ('korean_phone_like', re.compile(r'01[016789][- ]?\d{3,4}[- ]?\d{4}')),
    ('email_like', re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}')),
]
ALLOWLIST = {
    '.env.example',
    'scripts/secret_scan.py',
}

findings = []
for path in ROOT.rglob('*'):
    if any(part in SKIP_DIRS for part in path.parts):
        continue
    if not path.is_file():
        continue
    rel = path.relative_to(ROOT).as_posix()
    try:
        text = path.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        continue
    for name, pattern in PATTERNS:
        if rel in ALLOWLIST:
            continue
        for m in pattern.finditer(text):
            findings.append((rel, name, m.group(0)[:80]))

if findings:
    print('Potential private data found:')
    for rel, name, sample in findings:
        print(f'- {rel}: {name}: {sample}')
    sys.exit(1)

print('Secret scan OK')
