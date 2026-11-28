"""Generate the profile README artwork (dark + light SVGs) into ../assets.

Run:  python tools/gen.py
Every SVG is self-contained: system fonts only, CSS/SMIL animation, no scripts,
so GitHub renders it through <img>/<picture>.
"""
from pathlib import Path
from xml.sax.saxutils import escape as esc

OUT = Path(__file__).resolve().parent.parent / "assets"

SANS = "'Inter','Segoe UI Variable Display','Segoe UI',system-ui,-apple-system,'Helvetica Neue',Arial,sans-serif"
MONO = "'JetBrains Mono','SF Mono','Cascadia Code',Consolas,ui-monospace,Menlo,monospace"

THEMES = {
    "dark": dict(bg="#07090C", panel="#0E1217", panel2="#131820", line="#222A35",
                 text="#E8EDF2", muted="#8E99A6", dim="#465060", glow=0.30),
    "light": dict(bg="#F5F7FA", panel="#FFFFFF", panel2="#F0F3F7", line="#D9DFE6",
                  text="#141A21", muted="#5A6573", dim="#B4BDC8", glow=0.16),
}
BRAND = "#00C9A7"
ACC = {"phoecord": "#FF7A1A", "csa": "#22D39A", "zofu": "#5B8CFF", "vq": "#FF4655"}

CSS = """
.s{font-family:%(sans)s}.m{font-family:%(mono)s}
@keyframes flow{to{stroke-dashoffset:-20}}
.flow{stroke-dasharray:4 6;animation:flow 1.1s linear infinite}
@keyframes rise{from{opacity:0}to{opacity:1}}
.ln{opacity:0;animation:rise .45s ease-out forwards}
@keyframes blink{50%%{opacity:0}}.cur{animation:blink 1s step-end infinite}
@keyframes pulse{0%%,100%%{opacity:.35}50%%{opacity:1}}.pulse{animation:pulse 2.4s ease-in-out infinite}
@keyframes draw{from{stroke-dashoffset:900}to{stroke-dashoffset:0}}
.draw{stroke-dasharray:900;animation:draw 4s ease-out infinite alternate}
@keyframes ring{from{stroke-dashoffset:0}to{stroke-dashoffset:163}}
.ring{stroke-dasharray:163;animation:ring 6s linear infinite}
@media (prefers-reduced-motion:reduce){*{animation:none!important}.ln{opacity:1}}
""" % dict(sans=SANS, mono=MONO)


def svg(w, h, body, defs=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img"><defs><style>{CSS}</style>{defs}</defs>{body}</svg>\n')


def text(x, y, s, size=14, fill="#000", cls="s", weight=400, anchor="start", extra=""):
    return (f'<text x="{x}" y="{y}" class="{cls}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}" {extra}>{esc(s)}</text>')


def mono_w(s, size):  # monospace advance ~0.6em
    return len(s) * size * 0.6


def dots(pid, t, gap=22):
    return (f'<pattern id="{pid}" width="{gap}" height="{gap}" patternUnits="userSpaceOnUse">'
            f'<circle cx="2" cy="2" r="1" fill="{t["dim"]}" opacity=".55"/></pattern>')


def glow(gid, color, cx, cy, op):
    return (f'<radialGradient id="{gid}" cx="{cx}" cy="{cy}" r="65%">'
            f'<stop offset="0" stop-color="{color}" stop-opacity="{op}"/>'
            f'<stop offset="1" stop-color="{color}" stop-opacity="0"/></radialGradient>')


def panel(w, h, t, pid, gid, rx=20):
    return (f'<clipPath id="c{pid}"><rect x="1" y="1" width="{w-2}" height="{h-2}" rx="{rx}"/></clipPath>'
            , f'<g clip-path="url(#c{pid})"><rect width="{w}" height="{h}" fill="{t["panel"]}"/>'
              f'<rect width="{w}" height="{h}" fill="url(#{pid})"/><rect width="{w}" height="{h}" fill="url(#{gid})"/></g>'
              f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="{rx}" fill="none" stroke="{t["line"]}"/>')


def chips(x0, y0, items, t, color, maxx, size=12, pad=22):
    out, x, y = [], x0, y0
    for it in items:
        w = mono_w(it, size) + pad
        if x + w > maxx:
            x, y = x0, y + 34
        out.append(f'<rect x="{x}" y="{y}" width="{w:.0f}" height="26" rx="13" fill="{t["panel2"]}" stroke="{t["line"]}"/>')
        out.append(text(x + w / 2, y + 17.5, it, size, t["text"], "m", 500, "middle"))
        x += w + 8
    return "".join(out)


def pill(x, y, s, color, size=11):
    w = mono_w(s, size) + 20
    return (f'<rect x="{x}" y="{y}" width="{w:.0f}" height="22" rx="11" fill="{color}" fill-opacity=".12" '
            f'stroke="{color}" stroke-opacity=".45"/>'
            + text(x + w / 2, y + 15, s, size, color, "m", 600, "middle", 'letter-spacing="1"')), w


# ---------------------------------------------------------------- hero
def hero(t):
    W, H = 1000, 440
    defs = dots("hd", t) + glow("hg", BRAND, "88%", "0%", t["glow"]) + glow("hg2", ACC["zofu"], "0%", "100%", t["glow"] * .5)
    clip, base = panel(W, H, t, "hd", "hg")
    b = [clip.replace("<clipPath", "<clipPath") if False else "", base,
         f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="20" fill="url(#hg2)"/>']
    b.append(f'<circle cx="54" cy="57" r="4" fill="{BRAND}" class="pulse"/>')
    b.append(text(68, 62, "KENNURKEN  /  PORTFOLIO  /  2026", 12, t["muted"], "m", 500, extra='letter-spacing="2.5"'))
    b.append(f'<text x="42" y="196" class="s" font-size="132" font-weight="800" fill="{t["text"]}" letter-spacing="-5">ken<tspan fill="{BRAND}">.</tspan></text>')
    b.append(text(48, 246, "Backend & systems engineer", 26, t["text"], weight=650))
    b.append(text(48, 282, "I build the parts that have to be right: ledgers,", 17, t["muted"]))
    b.append(text(48, 306, "schedulers, realtime state and the tests that prove them.", 17, t["muted"]))
    # terminal
    tx, ty, tw, th = 560, 52, 400, 258
    b.append(f'<rect x="{tx}" y="{ty}" width="{tw}" height="{th}" rx="12" fill="{t["bg"]}" stroke="{t["line"]}"/>')
    b.append(f'<line x1="{tx}" y1="{ty+34}" x2="{tx+tw}" y2="{ty+34}" stroke="{t["line"]}"/>')
    for i, c in enumerate(["#FF5F57", "#FEBC2E", "#28C840"]):
        b.append(f'<circle cx="{tx+22+i*18}" cy="{ty+17}" r="5.5" fill="{c}"/>')
    b.append(text(tx + tw / 2, ty + 22, "~/ken — zsh", 12, t["muted"], "m", anchor="middle"))
    lines = [("$", "ken --stats"), ("", "1,678 tests across 4 flagship repos"), ("", "105k lines · Python, Rust, TypeScript"),
             ("$", "ken --now"), ("", "csa       live on AWS, 24/7"), ("", "phoecord  v0.7.0 · 9 Rust crates"),
             ("", "zofu      MVP · multi-tenant API")]
    y = ty + 64
    for i, (p, s) in enumerate(lines):
        d = f'style="animation-delay:{.3 + i*.38:.2f}s"'
        if p:
            b.append(f'<text x="{tx+20}" y="{y}" class="m ln" font-size="14" xml:space="preserve" {d}><tspan fill="{BRAND}" font-weight="700">$ </tspan><tspan fill="{t["text"]}">{esc(s)}</tspan></text>')
        else:
            b.append(f'<text x="{tx+20}" y="{y}" class="m ln" font-size="14" xml:space="preserve" fill="{t["muted"]}" {d}>  {esc(s)}</text>')
        y += 24
    d = f'style="animation-delay:{.3 + len(lines)*.38:.2f}s"'
    b.append(f'<g class="ln" {d}><text x="{tx+20}" y="{y}" class="m" font-size="14" fill="{BRAND}" font-weight="700">$</text>'
             f'<rect x="{tx+36}" y="{y-13}" width="9" height="16" fill="{BRAND}" class="cur"/></g>')
    # stats strip
    b.append(f'<line x1="48" y1="342" x2="952" y2="342" stroke="{t["line"]}"/>')
    stats = [("105k+", "lines in featured repos"), ("1,678", "automated tests"), ("4", "flagship products"), ("24/7", "CSA live on AWS EC2")]
    for i, (n, l) in enumerate(stats):
        x = 48 + i * 232
        b.append(text(x, 392, n, 36, t["text"], weight=800, extra='letter-spacing="-1"'))
        b.append(text(x, 414, l, 12, t["muted"], "m"))
    return svg(W, H, "".join(b), defs + clip)


# ---------------------------------------------------------------- section header
def section(num, title, right, t):
    W, H = 1000, 64
    tw = len(title) * 12.5
    b = [text(0, 42, num, 14, BRAND, "m", 700),
         text(38, 42, title, 24, t["text"], weight=750, extra='letter-spacing="-.5"'),
         f'<line x1="{38+tw+24:.0f}" y1="36" x2="{1000-mono_w(right,13)-20:.0f}" y2="36" stroke="{t["line"]}"/>',
         text(1000, 41, right, 13, t["muted"], "m", anchor="end")]
    return svg(W, H, "".join(b))


# ---------------------------------------------------------------- diagram helpers
def box(x, y, w, h, label, t, color, sub=None, hot=False, dashed=False):
    stroke = color if hot else t["line"]
    fill = f'fill="{color}" fill-opacity=".10"' if hot else f'fill="{t["panel"]}"'
    da = ' stroke-dasharray="4 4"' if dashed else ""
    s = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" {fill} stroke="{stroke}"{da}/>']
    ly = y + h / 2 + (-3 if sub else 4.5)
    s.append(text(x + w / 2, ly, label, 12.5, color if hot else t["text"], "m", 700, "middle"))
    if sub:
        s.append(text(x + w / 2, ly + 16, sub, 10, t["muted"], "m", 400, "middle"))
    return "".join(s)


def wire(d, color, packet=True, dur=2.2, rev=False):
    s = f'<path d="{d}" fill="none" stroke="{color}" stroke-opacity=".75" stroke-width="1.5" class="flow"/>'
    if packet:
        kp = ' keyPoints="1;0" keyTimes="0;1" calcMode="linear"' if rev else ""
        s += (f'<circle r="3.2" fill="{color}"><animateMotion dur="{dur}s" repeatCount="indefinite" path="{d}"{kp}/></circle>')
    return s


def diag_phoecord(t, c):
    g = [box(24, 36, 170, 54, "Discord client", t, c, "native · Rust/GPUI"),
         box(226, 36, 170, 54, "loader", t, c, "UI · themes · settings"),
         wire("M194 63 H226", c, False),
         box(24, 132, 372, 58, "phoecord-proxy", t, c, "rewrites REST + Gateway · local CA", hot=True),
         wire("M109 90 V132", c, dur=1.6),
         box(226, 232, 170, 54, "discord.com", t, c, "REST · WSS"),
         wire("M311 190 V232", c, dur=1.6), wire("M321 190 V232", c, dur=1.9, rev=True)]
    for i in range(3):
        g.append(box(24 + i * 58, 232, 50, 54, "wasm", t, c, f"plg{i+1}"))
    g.append(wire("M107 190 V232", c, dur=1.4))
    g.append(text(24, 306, "sandboxed plugins · WIT API", 10.5, t["muted"], "m"))
    return "".join(g)


def diag_csa(t, c):
    g = []
    row1 = ["binance", "dq ×13", "features", "strategy"]
    for i, s in enumerate(row1):
        g.append(box(20 + i * 100, 36, 84, 44, s, t, c, hot=(i == 0)))
        if i:
            g.append(wire(f"M{20+i*100-16} 58 H{20+i*100}", c, False))
    g.append(wire("M362 80 V124", c, dur=1.2))
    row2 = [("risk gate", True), ("paper", False), ("telegram", False)]
    for i, (s, hot) in enumerate(row2):
        x = 320 - i * 100
        g.append(box(x, 124, 84, 44, s, t, c, hot=hot))
        if i:
            g.append(wire(f"M{x+100} 146 H{x+84}", c, False))
    g.append(box(20, 124, 84, 44, "orders", t, t["dim"], "none", dashed=True))
    g.append(f'<line x1="36" y1="140" x2="88" y2="140" stroke="{t["muted"]}" stroke-width="1.2"/>')
    g.append(text(112, 151, "✕", 13, t["muted"], "m", 700, "middle"))
    pts = [(20, 292), (60, 284), (95, 288), (130, 270), (165, 276), (200, 255), (235, 262), (270, 240),
           (305, 246), (340, 226), (370, 232), (400, 214)]
    d = "M" + " L".join(f"{x} {y}" for x, y in pts)
    g.append(f'<path d="{d} L400 300 L20 300 Z" fill="{c}" fill-opacity=".07"/>')
    g.append(f'<path d="{d}" fill="none" stroke="{c}" stroke-width="2" class="draw"/>')
    g.append(text(20, 206, "backtest gates · deflated Sharpe · PBO", 10.5, t["muted"], "m"))
    return "".join(g)


def diag_zofu(t, c):
    g = [f'<rect x="34" y="34" width="62" height="108" rx="12" fill="{t["panel"]}" stroke="{t["line"]}"/>',
         f'<rect x="54" y="40" width="22" height="5" rx="2.5" fill="{t["line"]}"/>',
         f'<rect x="42" y="56" width="46" height="8" rx="3" fill="{c}" fill-opacity=".5"/>',
         f'<rect x="42" y="70" width="34" height="6" rx="3" fill="{t["line"]}"/>',
         f'<rect x="42" y="82" width="40" height="6" rx="3" fill="{t["line"]}"/>',
         text(65, 162, "students", 11, t["muted"], "m", anchor="middle"),
         f'<rect x="16" y="190" width="104" height="76" rx="8" fill="{t["panel"]}" stroke="{t["line"]}"/>',
         f'<line x1="16" y1="204" x2="120" y2="204" stroke="{t["line"]}"/>',
         "".join(f'<circle cx="{25+i*8}" cy="197" r="2.2" fill="{t["dim"]}"/>' for i in range(3)),
         f'<rect x="26" y="214" width="24" height="42" rx="3" fill="{t["line"]}"/>',
         f'<rect x="56" y="214" width="54" height="18" rx="3" fill="{c}" fill-opacity=".5"/>',
         f'<rect x="56" y="238" width="54" height="18" rx="3" fill="{t["line"]}"/>',
         text(68, 286, "curators · dean", 11, t["muted"], "m", anchor="middle"),
         box(160, 120, 118, 80, "api", t, c, "tenant-scoped", hot=True),
         wire("M96 88 C130 88 130 150 160 150", c, dur=1.8),
         wire("M120 228 C140 228 140 170 160 170", c, dur=2.0)]
    for i, n in enumerate(["uni A", "uni B", "uni C"]):
        y = 44 + i * 88
        g.append(f'<path d="M316 {y+8} a36 8 0 0 1 72 0 v40 a36 8 0 0 1 -72 0 z" fill="{t["panel"]}" stroke="{t["line"]}"/>'
                 f'<path d="M316 {y+8} a36 8 0 0 0 72 0" fill="none" stroke="{t["line"]}"/>')
        g.append(text(352, y + 36, n, 11.5, t["text"], "m", 600, "middle"))
        g.append(wire(f"M278 160 C300 160 296 {y+28} 316 {y+28}", c, dur=1.6 + i * .3))
    g.append(text(396, 26, "kk · ru · en", 10.5, t["muted"], "m", anchor="end"))
    return "".join(g)


def diag_vq(t, c):
    b2 = "#5B8CFF"
    g = [f'<circle cx="48" cy="58" r="22" fill="{c}" fill-opacity=".12" stroke="{c}"/>',
         text(48, 63, "A", 15, c, "m", 800, "middle"),
         text(84, 54, "coin flip", 12.5, t["text"], "m", 700),
         text(84, 71, "winner: ban first / pick side", 10.5, t["muted"], "m")]
    x0, w, gap = 18, 48, 8
    for i in range(7):
        x = x0 + i * (w + gap)
        d = f'style="animation-delay:{.4 + i*.45:.2f}s"'
        if i < 6:
            col = c if i % 2 == 0 else b2
            g.append(f'<g class="ln" {d}><rect x="{x}" y="112" width="{w}" height="68" rx="7" fill="{t["panel"]}" stroke="{col}" stroke-opacity=".6"/>'
                     f'<line x1="{x+10}" y1="126" x2="{x+w-10}" y2="166" stroke="{col}" stroke-opacity=".5" stroke-width="1.5"/>'
                     + text(x + w / 2, 196, "BAN", 10, col, "m", 700, "middle")
                     + text(x + w / 2, 150, "AB"[i % 2], 13, t["text"], "m", 700, "middle") + "</g>")
        else:
            g.append(f'<g class="ln" {d}><rect x="{x}" y="112" width="{w}" height="68" rx="7" fill="{c}" fill-opacity=".18" stroke="{c}" stroke-width="1.5"/>'
                     + text(x + w / 2, 150, "★", 16, c, "m", 700, "middle")
                     + text(x + w / 2, 196, "PICK", 10, c, "m", 800, "middle") + "</g>")
    g.append(f'<circle cx="48" cy="262" r="26" fill="none" stroke="{t["line"]}" stroke-width="4"/>'
             f'<circle cx="48" cy="262" r="26" fill="none" stroke="{c}" stroke-width="4" class="ring" transform="rotate(-90 48 262)"/>'
             + text(48, 267, "30s", 12, t["text"], "m", 700, "middle"))
    for i, s in enumerate(["pure state machine · applyAction()", "versioned writes: one click wins", "timeouts settle on read, no cron"]):
        g.append(text(92, 248 + i * 19, s, 11, t["muted"], "m"))
    return "".join(g)


PROJECTS = [
    dict(key="phoecord", idx="01", title="PhoeCord", pills=["OPEN SOURCE", "PRE-ALPHA"],
         tag=["Plugin loader for Discord's new native client.", "No JavaScript to patch, so a local proxy rewrites",
              "REST/Gateway traffic and plugins run as WASM."],
         metrics=[("9", "rust crates"), ("279", "tests"), ("22k", "lines of rust")],
         stack=["Rust", "WASM", "WIT", "GPUI", "TLS/MITM", "Tokio"], diagram=diag_phoecord),
    dict(key="csa", idx="02", title="CSA", pills=["PRIVATE", "LIVE 24/7"],
         tag=["Crypto swing-trading analyst on Binance public", "data. Rules, risk gate and paper ledger, with",
              "statistical backtest gates. It never places orders."],
         metrics=[("1,233", "tests"), ("52k", "lines of python"), ("13", "data-quality checks")],
         stack=["Python", "SQLite", "Parquet", "aiogram 3", "Docker", "AWS EC2", "S3"], diagram=diag_csa),
    dict(key="zofu", idx="03", title="Zofu", pills=["PRIVATE", "MVP"],
         tag=["University platform: a mobile app for students and", "a web cabinet for curators and the dean's office.",
              "One API, each university isolated as a tenant."],
         metrics=[("107", "tests"), ("4", "shared packages"), ("3", "languages")],
         stack=["TypeScript", "Next.js", "FastAPI", "pnpm", "Turbo", "Docker", "CI"], diagram=diag_zofu),
    dict(key="vq", idx="04", title="Val Qauym", pills=["PRIVATE", "REALTIME"],
         tag=["Tournament tooling for a Kazakh VALORANT community:", "solo sign-ups, rank-balanced team builder and a",
              "live Faceit-style map veto for captains and stream."],
         metrics=[("2", "apps"), ("59", "tests"), ("24k", "lines of ts")],
         stack=["Next.js", "TypeScript", "Supabase", "Realtime", "Tailwind", "Vercel"], diagram=diag_vq),
]


def card(p, t):
    W, H = 1000, 400
    c = ACC[p["key"]]
    pid, gid = f"d{p['key']}", f"g{p['key']}"
    defs = dots(pid, t) + glow(gid, c, "0%", "0%", t["glow"]) + dots(pid + "i", t, 18)
    clip, base = panel(W, H, t, pid, gid)
    b = [base, f'<rect x="40" y="0" width="120" height="3" rx="1.5" fill="{c}"/>']
    b.append(text(48, 64, f"{p['idx']} / 04", 13, c, "m", 700, extra='letter-spacing="1"'))
    x = 128
    for s in p["pills"]:
        el, w = pill(x, 49, s, c)
        b.append(el)
        x += w + 8
    b.append(text(46, 130, p["title"], 50, t["text"], weight=800, extra='letter-spacing="-1.5"'))
    for i, s in enumerate(p["tag"]):
        b.append(text(48, 170 + i * 26, s, 17, t["muted"]))
    for i, (n, l) in enumerate(p["metrics"]):
        x = 48 + i * 158
        b.append(text(x, 288, n, 32, c, weight=800, extra='letter-spacing="-1"'))
        b.append(text(x, 310, l, 11.5, t["muted"], "m"))
    b.append(chips(48, 336, p["stack"], t, c, 530, 11, 18))
    # diagram panel
    b.append(f'<g transform="translate(548 40)"><rect width="412" height="320" rx="14" fill="{t["bg"]}" stroke="{t["line"]}"/>'
             f'<rect width="412" height="320" rx="14" fill="url(#{pid}i)" opacity=".7"/>'
             + text(14, 22, "fig. " + p["idx"], 10.5, t["dim"], "m", 600)
             + p["diagram"](t, c) + "</g>")
    return svg(W, H, "".join(b), defs + clip)


# ---------------------------------------------------------------- small tiles
TILES = [
    ("wallet", "Java", "Double-entry ledger, row-locked idempotent", "transfers, rotating JWT refresh.", "1000 parallel transfers, books balance", BRAND),
    ("qalqan-ai", "Python", "Anti-fraud API: Redis cache → threat DBs →", "fine-tuned XLM-R → LLM. Ext + PWA + bot.", "7-tier detection pipeline", ACC["csa"]),
    ("kazgpt", "Python · Java", "Offline Kazakh assistant. Qwen2.5-7B QLoRA", "on KazQAD behind Spring WebFlux streaming.", "runs fully local via Ollama", ACC["zofu"]),
    ("tender-tracker", "TypeScript", "goszakup.gov.kz lots closing within 2 hours", "with 0–1 bidders. Live dashboard.", "Next.js + Supabase", ACC["phoecord"]),
    ("LiveWall", "Swift", "Live wallpapers for macOS: video, web pages,", "GLSL shaders and interactive scenes.", "native macOS app in Swift", ACC["vq"]),
    ("+ more", "16 public repos", "Flutter apps, FastAPI services, CLI tools,", "university labs and experiments.", "see all repositories →", BRAND),
]


def tile(name, lang, d1, d2, foot, c, t):
    W, H = 480, 168
    pid, gid = "td", "tg"
    defs = dots(pid, t, 20) + glow(gid, c, "100%", "0%", t["glow"] * .8)
    clip, base = panel(W, H, t, pid, gid, 16)
    b = [base, f'<rect x="24" y="30" width="10" height="10" rx="2" fill="{c}"/>',
         text(44, 40, name, 21, t["text"], weight=750, extra='letter-spacing="-.4"'),
         text(W - 24, 39, lang, 11.5, t["muted"], "m", anchor="end"),
         text(24, 80, d1, 14.5, t["muted"]), text(24, 102, d2, 14.5, t["muted"]),
         f'<line x1="24" y1="124" x2="{W-24}" y2="124" stroke="{t["line"]}"/>',
         text(24, 148, foot, 12, c, "m", 600)]
    return svg(W, H, "".join(b), defs + clip)


# ---------------------------------------------------------------- stack
STACK = [("Backend", ["Java 21", "Spring Boot", "WebFlux", "Python", "FastAPI", "SQLAlchemy", "aiogram", "JWT"]),
         ("Systems & clients", ["Rust", "Tokio", "WASM", "TypeScript", "Next.js", "Flutter", "Swift", "Tailwind"]),
         ("Data & infra", ["PostgreSQL", "Redis", "SQLite", "Supabase", "Docker", "AWS", "GitHub Actions", "Vercel"])]


def stack(t):
    W, H = 1000, 200
    defs = dots("sd", t) + glow("sg", BRAND, "50%", "0%", t["glow"] * .6)
    clip, base = panel(W, H, t, "sd", "sg")
    b = [base]
    for i, (h, items) in enumerate(STACK):
        x = 40 + i * 320
        b.append(text(x, 58, h.upper(), 12, BRAND, "m", 700, extra='letter-spacing="2"'))
        b.append(chips(x, 78, items, t, BRAND, x + 300, 12.5))
    return svg(W, H, "".join(b), defs + clip)


# ---------------------------------------------------------------- footer
def footer(t):
    W, H = 1000, 190
    defs = dots("fd", t) + glow("fg", BRAND, "100%", "100%", t["glow"])
    clip, base = panel(W, H, t, "fd", "fg")
    b = [base,
         f'<text x="990" y="210" class="s" font-size="230" font-weight="800" fill="{t["text"]}" fill-opacity=".04" text-anchor="end" letter-spacing="-10">ken.</text>',
         text(48, 86, "Got something that has to be right?", 32, t["text"], weight=800, extra='letter-spacing="-1"'),
         text(48, 122, "Backends, data pipelines, realtime systems. Telegram is the fastest way to reach me.", 16.5, t["muted"]),
         f'<circle cx="54" cy="152" r="4" fill="{BRAND}" class="pulse"/>',
         text(68, 157, "KAZAKHSTAN · RU / KK / EN", 12, t["muted"], "m", 500, extra='letter-spacing="2"')]
    return svg(W, H, "".join(b), defs + clip)


def main():
    OUT.mkdir(exist_ok=True)
    for name, t in THEMES.items():
        files = {"hero": hero(t), "stack": stack(t), "footer": footer(t),
                 "sec-work": section("01", "Selected work", "4 flagship projects", t),
                 "sec-more": section("02", "Also built", "16 public repos", t),
                 "sec-stack": section("03", "Stack", "what I reach for", t),
                 "sec-activity": section("04", "Activity", "updated daily", t)}
        for p in PROJECTS:
            files[f"card-{p['key']}"] = card(p, t)
        for i, tl in enumerate(TILES):
            files[f"tile-{i+1}"] = tile(*tl, t)
        for k, v in files.items():
            (OUT / f"{k}-{name}.svg").write_text(v, encoding="utf-8")
    print("wrote", len(list(OUT.glob("*.svg"))), "files to", OUT)


if __name__ == "__main__":
    main()
