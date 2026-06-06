#!/usr/bin/env python3
from pathlib import Path
import html

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "docs" / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)

BG = "#231E1B"
PAPER = "#D9D9D9"
INK = "#231E1B"
MUTED = "#6B625D"
ACCENT = "#F2C14E"
BLUE = "#89B4FA"
GREEN = "#A6E3A1"
ROSE = "#F38BA8"
VIOLET = "#CBA6F7"
LINE = "#8E827A"


def svg_wrap(title, body, w=1200, h=675):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{html.escape(title)}">
  <defs>
    <pattern id="hatch" width="12" height="12" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
      <line x1="0" y1="0" x2="0" y2="12" stroke="#3a332f" stroke-width="2" opacity="0.45"/>
    </pattern>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="12" stdDeviation="10" flood-color="#000000" flood-opacity="0.22"/>
    </filter>
    <style>
      .title {{ font: 800 42px -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; fill: {PAPER}; letter-spacing: -1px; }}
      .subtitle {{ font: 500 21px -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; fill: #cfc7c1; }}
      .label {{ font: 800 24px -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; fill: {INK}; }}
      .small {{ font: 600 17px -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; fill: {MUTED}; }}
      .tiny {{ font: 600 14px -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; fill: {MUTED}; }}
      .mono {{ font: 600 16px ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; fill: {INK}; }}
      .monoSmall {{ font: 600 13px ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; fill: {MUTED}; }}
    </style>
  </defs>
  <rect width="1200" height="675" fill="{BG}"/>
  <rect width="1200" height="675" fill="url(#hatch)" opacity="0.35"/>
  {body}
</svg>
'''


def card(x, y, w, h, fill=PAPER, stroke="#ffffff", rx=26):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="2" filter="url(#shadow)"/>'


def arrow(x1, y1, x2, y2, color=PAPER):
    return f'''<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="5" stroke-linecap="round"/>
<path d="M {x2} {y2} l -14 -9 l 0 18 z" fill="{color}" transform="rotate({0 if x2>=x1 else 180} {x2} {y2})"/>'''


def make_flow():
    items = [
        (70, 240, "아이디어", "하고 싶은 일"),
        (255, 240, "작업 요청", "Issue/Handoff"),
        (440, 240, "AI 역할", "리서처/빌더/리뷰어"),
        (625, 240, "작업 진행", "근거 남기기"),
        (810, 240, "사람 검토", "확인과 수정"),
        (995, 240, "재사용", "다음 프로젝트로"),
    ]
    body = '<text x="70" y="85" class="title">AI를 챗봇이 아니라 작은 팀처럼 운영하기</text>\n'
    body += '<text x="72" y="122" class="subtitle">요청 → 역할 → 기록 → 검토 → 재사용까지 한 흐름으로 묶습니다</text>\n'
    for i, (x, y, t, s) in enumerate(items):
        body += card(x, y, 135, 135, PAPER, "#f6f0e8", 28) + "\n"
        body += f'<circle cx="{x+67}" cy="{y+42}" r="22" fill="{[ACCENT,BLUE,GREEN,VIOLET,ROSE,ACCENT][i]}"/>\n'
        body += f'<text x="{x+67}" y="{y+50}" text-anchor="middle" class="label" font-size="24">{i+1}</text>\n'
        body += f'<text x="{x+67}" y="{y+89}" text-anchor="middle" class="label">{t}</text>\n'
        body += f'<text x="{x+67}" y="{y+116}" text-anchor="middle" class="tiny">{s}</text>\n'
        if i < len(items)-1:
            body += arrow(x+145, y+67, x+175, y+67, "#e7ded7") + "\n"
    body += '<rect x="170" y="455" width="860" height="95" rx="24" fill="#D9D9D9" opacity="0.96"/>\n'
    body += f'<text x="600" y="500" text-anchor="middle" class="label">핵심은 프롬프트보다 운영 방식입니다</text>\n'
    body += f'<text x="600" y="530" text-anchor="middle" class="small">AI가 한 일을 문서로 남기고, 사람이 마지막에 검토합니다</text>\n'
    return svg_wrap("AI Team Flow", body)


def make_fork():
    body = '<text x="70" y="82" class="title">GitHub에서 내 복사본 만들기</text>\n'
    body += '<text x="72" y="118" class="subtitle">오른쪽 위 Fork 버튼을 누르면 내 계정에 템플릿이 복사됩니다</text>\n'
    body += card(80, 170, 1040, 390, "#F3EEE8", "#ffffff", 30)
    body += '<rect x="80" y="170" width="1040" height="62" rx="30" fill="#E4DDD6"/>\n'
    body += '<circle cx="120" cy="201" r="9" fill="#F38BA8"/><circle cx="148" cy="201" r="9" fill="#F2C14E"/><circle cx="176" cy="201" r="9" fill="#A6E3A1"/>\n'
    body += '<text x="110" y="282" class="label">bluealmond33-debug / ai-team-ops-template</text>\n'
    body += '<rect x="865" y="255" width="165" height="54" rx="16" fill="#231E1B"/>\n'
    body += '<text x="947" y="290" text-anchor="middle" style="font:800 22px sans-serif; fill:#D9D9D9;">Fork</text>\n'
    body += '<path d="M 825 360 C 875 320, 905 315, 940 310" fill="none" stroke="#F2C14E" stroke-width="8" stroke-linecap="round"/>\n'
    body += '<path d="M 940 310 l -22 0 l 15 -17 z" fill="#F2C14E"/>\n'
    body += '<rect x="180" y="360" width="380" height="104" rx="22" fill="#D9D9D9" stroke="#231E1B" stroke-width="2"/>\n'
    body += '<text x="370" y="405" text-anchor="middle" class="label">1분이면 시작</text>\n'
    body += '<text x="370" y="437" text-anchor="middle" class="small">설치보다 먼저 복사해서 구조를 보세요</text>\n'
    body += '<text x="948" y="372" text-anchor="middle" style="font:800 26px sans-serif; fill:#231E1B;">여기를 클릭</text>\n'
    return svg_wrap("GitHub Fork Guide", body)


def make_handoff():
    body = '<text x="70" y="82" class="title">AI에게 일을 맡기고 넘겨받는 양식</text>\n'
    body += '<text x="72" y="118" class="subtitle">말로 흘려보내지 않고, 목표·근거·검증을 남깁니다</text>\n'
    body += card(95, 160, 1010, 420, "#F3EEE8", "#ffffff", 28)
    body += '<text x="135" y="220" class="label">HANDOFF</text>\n'
    sections=[("목표", "README를 KDA4 비개발자도 이해하게 개선"), ("담당", "Researcher → Builder → Reviewer"), ("근거", "읽은 파일, 실행한 검증, 남은 위험"), ("완료 조건", "README 반영 + secret scan OK + push 완료")]
    y=260
    colors=[ACCENT,BLUE,GREEN,ROSE]
    for idx,(k,v) in enumerate(sections):
        body += f'<rect x="135" y="{y}" width="930" height="58" rx="16" fill="#D9D9D9" stroke="{colors[idx]}" stroke-width="4"/>\n'
        body += f'<text x="160" y="{y+36}" class="label" font-size="22">{k}</text>\n'
        body += f'<text x="300" y="{y+36}" class="small">{v}</text>\n'
        y += 76
    return svg_wrap("Handoff Example", body)


def make_issue():
    body = '<text x="70" y="82" class="title">작업은 Issue처럼 작게 쪼개기</text>\n'
    body += '<text x="72" y="118" class="subtitle">큰 요청을 바로 실행하지 말고, 확인 가능한 단위로 나눕니다</text>\n'
    body += card(90, 155, 1020, 430, "#F3EEE8", "#ffffff", 28)
    body += '<text x="135" y="215" class="label">#001 프로젝트 소개 문서 만들기</text>\n'
    body += '<rect x="135" y="245" width="150" height="34" rx="17" fill="#A6E3A1"/><text x="210" y="268" text-anchor="middle" class="tiny" fill="#231E1B">good first task</text>\n'
    body += '<rect x="305" y="245" width="95" height="34" rx="17" fill="#89B4FA"/><text x="352" y="268" text-anchor="middle" class="tiny">docs</text>\n'
    items=["무엇을 만들지 5줄로 설명", "대상 사용자를 3개 bullet로 정리", "완료 조건과 검증 방법 작성", "AI가 참고한 파일/근거 남기기"]
    y=325
    for item in items:
        body += f'<rect x="140" y="{y-24}" width="26" height="26" rx="6" fill="#D9D9D9" stroke="#231E1B" stroke-width="3"/>\n'
        body += f'<path d="M146 {y-10} l7 8 l17 -20" fill="none" stroke="#231E1B" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>\n'
        body += f'<text x="185" y="{y}" class="small">{item}</text>\n'
        y += 55
    body += '<rect x="760" y="315" width="270" height="130" rx="22" fill="#231E1B"/>\n'
    body += '<text x="895" y="363" text-anchor="middle" style="font:800 25px sans-serif; fill:#D9D9D9;">작게 나누면</text>\n'
    body += '<text x="895" y="398" text-anchor="middle" style="font:700 20px sans-serif; fill:#cfc7c1;">AI 결과를 검증하기 쉽다</text>\n'
    return svg_wrap("Issue Example", body)


def make_obsidian():
    body = '<text x="70" y="82" class="title">기록은 노트처럼 쌓기</text>\n'
    body += '<text x="72" y="118" class="subtitle">결정, 회고, 학습을 다음 프로젝트에서 다시 찾을 수 있게 만듭니다</text>\n'
    body += card(110, 155, 980, 430, "#F3EEE8", "#ffffff", 28)
    folders=[("00 Inbox", "들어온 자료"), ("01 Projects", "진행 중 작업"), ("02 Decisions", "중요 결정"), ("03 Research", "조사와 근거"), ("04 Worklogs", "AI 작업 기록"), ("05 Retros", "회고와 개선")]
    x1,y1=160,230
    for i,(name,desc) in enumerate(folders):
        x = x1 + (i%2)*455
        y = y1 + (i//2)*95
        body += f'<rect x="{x}" y="{y}" width="370" height="64" rx="18" fill="#D9D9D9" stroke="#231E1B" stroke-width="2"/>\n'
        body += f'<path d="M{x+22} {y+22} h65 l14 14 h-79 z" fill="{[ACCENT,BLUE,GREEN,ROSE,VIOLET,ACCENT][i]}" opacity="0.95"/>\n'
        body += f'<text x="{x+115}" y="{y+31}" class="label" font-size="21">{name}</text>\n'
        body += f'<text x="{x+115}" y="{y+54}" class="tiny">{desc}</text>\n'
    body += '<text x="600" y="540" text-anchor="middle" style="font:800 24px sans-serif; fill:#231E1B;">AI가 한 일을 기록으로 남겨야 운영 방식이 자산이 됩니다</text>\n'
    return svg_wrap("Obsidian Vault Example", body)

files = {
    "ai-team-flow.svg": make_flow(),
    "github-fork-guide.svg": make_fork(),
    "handoff-example.svg": make_handoff(),
    "issue-example.svg": make_issue(),
    "obsidian-vault-example.svg": make_obsidian(),
}
for name, content in files.items():
    (ASSETS / name).write_text(content, encoding="utf-8")
    print(ASSETS / name)
