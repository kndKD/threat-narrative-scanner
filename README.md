# Threat Narrative Scanner

**Innovation: LLM Threat Narrative Generator**

Scan the Project 1/2 Flask app with Nmap + Wireshark/tshark, then turn
the raw output into a readable report: an executive summary a
non-technical reader can follow, plus a technical remediation plan —
in JSON and Markdown.

## Purpose

Raw scan output is a wall of ports and packets. This project makes it
a story: what is exposed, how bad is it, and what do you fix first.

## Architecture

See [docs/architecture.md](docs/architecture.md) — Nmap XML + tshark
stats → parser → rule-based risk rating → LLM narrative → `report.md`
+ `report.json`.

## Safety rule (hard)

Scan ONLY the user's own app — localhost, or the user's own free-tier
host from Project 2. Never scan a third-party host, and never scan an
address the user has not approved for this project.

## Tools used

Python 3.12, Nmap, tshark (Wireshark), pytest, ruff, GitHub Actions.
The LLM narrative uses Ollama locally (free); OpenAI/Gemini optional
via secret. No paid tools.

## Run locally

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
python -m pytest -q
python app/main.py
# Scan only your own app:
# nmap -sV -oX data/scan.xml 127.0.0.1
```

## Status (Day 1)

The Project 1 app is copied in as the scan target, with a sample Nmap
XML (`data/sample_nmap.xml`) so CI can run without nmap installed.
The parser lands Day 2, tshark stats Day 3, risk ratings Day 4,
the LLM narrative Day 5, and the first live scan of the user's own app
Day 6.

## Measurable impact

- Report writing time before (manual, timed) vs after (script run,
  timed) — measured during the week, not invented. The "2 hours →
  5 minutes" claim is not made until it is timed.

## What I learned

- _To be filled in as the project runs._

## Challenges

- _To be filled in as the project runs._
