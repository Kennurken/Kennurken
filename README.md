<div align="center">

  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:00C9A7,50:0B7A5C,100:00C9A7&height=220&section=header&text=Hi,%20I'm%20ken&fontSize=65&fontAlignY=35&desc=Backend%20Developer%20%7C%20Java%20%C2%B7%20Spring%20Boot%20%C2%B7%20Python&descAlignY=56&descAlign=50&fontColor=FFFFFF" alt="Header" />

  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=21&pause=1200&color=00C9A7&center=true&vCenter=true&width=700&lines=Building+transactional+backends+in+Spring+Boot;Double-entry+ledgers%2C+locking+and+idempotency;Async+APIs+with+FastAPI%2C+WebSockets+and+Redis;Serving+LLMs+behind+streaming+APIs" alt="Typing SVG" />
  </a>

  <br>

  <a href="mailto:kmarukob76@gmail.com">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" />
  </a>
  <a href="https://t.me/ken0543278">
    <img src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram" />
  </a>

  <br>

  <h2>🚀 About Me</h2>

  <p align="center">
    Backend developer from Kazakhstan. I build APIs, ledgers, data pipelines<br>
    and the services that sit behind AI products: auth, caching, queues, migrations, tests, Docker.
  </p>

  <table align="center">
    <tr>
      <td align="left">
        🌱 <b>Currently building:</b> a Spring Boot wallet / ledger service with JWT, row locking and idempotent transfers<br>
        🎯 <b>Main stack:</b> Java 21 · Spring Boot · PostgreSQL · Redis · Docker<br>
        💬 <b>Ask me about:</b> REST API design, transactions and concurrency, FastAPI, LLM serving<br>
        📫 <b>Contact:</b> Telegram or Email
      </td>
    </tr>
  </table>

  <h2>🏗️ Backend Work</h2>

</div>

| Project | Backend side | Stack |
|---|---|---|
| 💳 [**Wallet**](https://github.com/Kennurken/wallet) | Wallet / ledger service. Double-entry postings, transfers with `SELECT … FOR UPDATE` and retry, idempotency keys, JWT with rotating refresh tokens. Concurrency test runs 1000 parallel transfers and checks the ledger still balances; k6 load test results in the README. | Java 21 · Spring Boot · PostgreSQL · Docker · k6 |
| 🛡️ [**Qalqan AI**](https://github.com/Kennurken/qalqan-ai) · [live](https://qalqan-ai-nu.vercel.app) · [bot](https://t.me/QalqanAI_bot) | Anti-fraud API: 7-tier detection pipeline (whitelist → Redis cache → offline threat DBs → PhishTank/Safe Browsing → fine-tuned XLM-RoBERTa → LLM), partner API with key auth, PDF reports. One backend serves a browser extension, a PWA and a Telegram bot. | FastAPI · Upstash Redis · Groq/Gemini · Vercel |
| 🧠 [**KazGPT**](https://github.com/Kennurken/kazgpt-ai-assistant) | Spring Boot service in front of a local Kazakh LLM: streaming chat over WebFlux, response cache, typed config. Model: Qwen2.5-7B, QLoRA on KazQAD. | Spring Boot · WebFlux · Ollama |
| 🛵 [**Food Delivery**](https://github.com/Kennurken/food-delivery) · [live](https://food-delivery-drab-theta.vercel.app) | REST + WebSocket API with customer / courier / admin roles, live order status, Alembic migrations, tests, Docker. | FastAPI · SQLAlchemy · Alembic · Docker |
| 📊 [**Tender Tracker**](https://github.com/Kennurken/tender-tracker) | Ingests goszakup.gov.kz lots and surfaces the ones closing within 2 hours with 0–1 bidders. | Next.js API routes · Supabase Postgres |

<div align="center">

  <h2>🧰 Small Tools</h2>

</div>

- [**webchat-sales-desk**](https://github.com/Kennurken/webchat-sales-desk) — chat widget backend: FAQ, lead intake to SQLite, Slack/WhatsApp alerts
- [**pdf-toolkit**](https://github.com/Kennurken/pdf-toolkit) — CLI to merge, split, watermark PDFs and fill AcroForms from CSV
- [**messy-data-parser**](https://github.com/Kennurken/messy-data-parser) — cleans broken CSV/Excel exports into a tidy workbook + PDF summary

<div align="center">

  <h2>🛠️ Technical Arsenal</h2>

  <h4>Languages & Frameworks</h4>
  <p>
    <img src="https://skillicons.dev/icons?i=java,spring,python,fastapi&theme=dark" alt="Languages & Frameworks" />
  </p>

  <h4>Databases & Caching</h4>
  <p>
    <img src="https://skillicons.dev/icons?i=postgres,mysql,redis,sqlite,supabase&theme=dark" alt="Databases & Caching" />
  </p>

  <h4>DevOps & Tools</h4>
  <p>
    <img src="https://skillicons.dev/icons?i=docker,linux,bash,maven,git,github,githubactions,vercel,postman&theme=dark" alt="DevOps & Tools" />
  </p>

  <h2>📊 GitHub Analytics</h2>

  <img height="165" src="https://github-readme-streak-stats.herokuapp.com/?user=Kennurken&theme=transparent&hide_border=true&ring=00C9A7&fire=00C9A7&currStreakLabel=00C9A7&sideLabels=FFFFFF&dates=777777" alt="GitHub Streak" />

  <h2>📈 Contribution Activity</h2>

  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Kennurken/Kennurken/output/github-contribution-grid-snake-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Kennurken/Kennurken/output/github-contribution-grid-snake.svg">
    <img alt="GitHub Contribution Snake" src="https://raw.githubusercontent.com/Kennurken/Kennurken/output/github-contribution-grid-snake.svg">
  </picture>

  <h2>⚡ Engineering Focus</h2>

  <p>
    <code>REST API Design</code>
    <code>Transactions & Concurrency</code>
    <code>Auth & Security</code>
    <code>Caching</code>
    <code>Data Pipelines</code>
    <code>LLM Serving</code>
    <code>Testing</code>
  </p>

  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:00C9A7,50:0B7A5C,100:00C9A7&height=100&section=footer" alt="Footer" />

</div>
