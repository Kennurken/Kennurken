<div align="center">

# ken

**Backend developer. Java · Spring Boot · Python · FastAPI · PostgreSQL.**

I build APIs, data pipelines and services behind AI products for Kazakhstan.

</div>

## Backend work

| Project | Backend side | Stack |
|---|---|---|
| [**Qalqan AI**](https://github.com/Kennurken/qalqan-ai) · [live](https://qalqan-ai-nu.vercel.app) · [bot](https://t.me/QalqanAI_bot) | Anti-fraud API for Kazakhstan: 7-tier detection pipeline (whitelist → Redis cache → offline threat DBs → PhishTank/Safe Browsing → fine-tuned XLM-RoBERTa → LLM), partner API with key auth, PDF reports. One backend serves a browser extension, a PWA and a Telegram bot. | FastAPI · Upstash Redis · Groq/Gemini · Vercel |
| [**Food Delivery**](https://github.com/Kennurken/food-delivery) · [live](https://food-delivery-drab-theta.vercel.app) | REST + WebSocket API with customer / courier / admin roles, live order status, Alembic migrations, tests, Docker. | FastAPI · SQLAlchemy · Alembic · Docker |
| [**KazGPT**](https://github.com/Kennurken/kazgpt-ai-assistant) | Spring Boot service in front of a local Kazakh LLM: streaming chat over WebFlux, response cache, typed config. Model: Qwen2.5-7B, QLoRA on KazQAD. | Spring Boot · WebFlux · Ollama |
| [**Tender Tracker**](https://github.com/Kennurken/tender-tracker) | Ingests goszakup.gov.kz lots and surfaces the ones closing within 2 hours with 0–1 bidders. | Next.js API routes · Supabase Postgres |

## Small tools

- [**webchat-sales-desk**](https://github.com/Kennurken/webchat-sales-desk) — chat widget backend: FAQ, lead intake to SQLite, Slack/WhatsApp alerts
- [**pdf-toolkit**](https://github.com/Kennurken/pdf-toolkit) — CLI to merge, split, watermark PDFs and fill AcroForms from CSV
- [**messy-data-parser**](https://github.com/Kennurken/messy-data-parser) — cleans broken CSV/Excel exports into a tidy workbook + PDF summary
- [**form-to-sheet-notify**](https://github.com/Kennurken/form-to-sheet-notify) — Apps Script: validate form replies, notify Telegram, email fallback

## Stack

![Java](https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white)
![Spring](https://img.shields.io/badge/Spring_Boot-6DB33F?style=flat-square&logo=springboot&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![PHP](https://img.shields.io/badge/PHP-777BB4?style=flat-square&logo=php&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=flat-square&logo=supabase&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram_Bot_API-26A5E4?style=flat-square&logo=telegram&logoColor=white)
