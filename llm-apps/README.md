# llm-apps

The building track: small, working scripts on the Claude API, heading for **Milestone 1**:
a multi-turn chat loop + a resume screener that returns valid JSON + streaming.

**Rules for this folder**
- Count *sessions*, not days. One session = 45 minutes = one artifact (a script that runs, or a note).
- Bad day? The 10-minute floor still counts.
- Only the next session matters. Everything in "Parked" stays parked until Milestone 1 is done.

---

## Where I am (read once, at the start of Session 1)

**What I set out to do.** Move into AI application engineering — building systems that *use* LLMs, not training them.
In March–April 2026 I designed a 14-day sprint (Phase 1 of a 5-phase roadmap): API basics → prompt engineering →
structured output → tool use & MCP → RAG → agents → evals → deployed demo, followed by CCA Foundations exam prep.

**What I actually built** (originals in `~/dev/aiengineer/ai-sprint/`, copied into [`00-foundations/`](00-foundations/)):

| File | When | What it shows |
|---|---|---|
| `first_call.py` | Mar 24 | First API call, streaming the response token by token |
| `001_requests.ipynb` | Apr 18 | Academy exercises: multi-turn helpers, system prompts, temperature, streaming, structured JSON output |
| `chat_loop.py` (was `day2.py`) | Apr 19 | Stateful CLI chat loop — history kept in a Python list, resent each call |

**What I learned along the way**
- `system` is a top-level parameter, never an entry inside `messages`.
- The API is stateless: multi-turn = resend the whole history every call.
- `stop_reason` tells you *why* the model stopped (end of turn, max tokens, tool use, stop sequence).
- Also: CCA study on agent/tool-use concepts; Claude Code workflows; Track 1 Lesson 1 tokenizer notes (Sept, in `../llm-learning/`).

**Where that leaves me.** Sprint Days 1–2 are done. The next build task is the resume screener (sprint Day 3).
Then I stopped. That's fine — the code above still runs, and this picks up from it.

---

## Session 0 — setup (only if needed, ~5 min)

```bash
cd ~/dev/ai-engineer/llm-apps
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp ~/dev/aiengineer/ai-sprint/.env .env      # your existing API key; .env is gitignored
python 00-foundations/chat_loop.py           # sanity check — say hi, then quit
```

If the API rejects a model name (these scripts are from spring), swap in a current one.

---

## The next 5 sessions

### Session 1 — Recap + resume screener v0
- Read "Where I am" above (10 min).
- Write `01-resume-screener/screener.py`: read `inputs/jd.txt` and `inputs/resume.txt`, ask Claude for a fit score (1–10) with reasoning. Plain text output is fine.
- **Done when:** it runs on one real job posting and one made-up resume.
- **10-min floor:** run `chat_loop.py` once.

### Session 2 — Prompt variations
- Three system prompts: (a) bare, (b) role + criteria, (c) criteria + scoring rubric. Run each 3× on the same input.
- Log results in `01-resume-screener/prompt_log.md`.
- **Done when:** 9 runs logged + one line on which prompt won and why.
- **10-min floor:** 2 variations, once each.

### Session 3 — Strict JSON
- Return `{score, strengths, gaps, reasoning}`; parse with `json.loads`. Handle malformed output: catch, retry once, or fail with a clear message.
- You already did structured output in `001_requests.ipynb` — reuse that technique.
- **Done when:** result is a Python dict, and a deliberately broken response doesn't crash it.
- **10-min floor:** get JSON back and print it, no error handling yet.

### Session 4 — Edge cases + streaming
- Run the screener on 3 resumes: strong match, weak match, wrong field. Do the scores make sense?
- `chat_loop.py` uses `messages.create` — switch it to streaming (same pattern as `first_call.py`) and handle a stream error.
- **Done when:** 3 sensible scores; chat loop streams.
- **10-min floor:** the 3-resume test only.

### Session 5 — Milestone 1 + commit
- Check: chat loop works, screener returns valid JSON, streaming works.
- Add `01-resume-screener/README.md` (5 lines: what it does, how to run, one thing learned).
- Write 3 short "what surprised me" notes — future interview talking points.
- Commit and push.
- **Done when:** pushed.
- **10-min floor:** commit locally; README later.

---

## Session log

| # | Date | Done? | One-line note |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

---

## Parked (not cancelled — just off the board until Milestone 1)
- Track 1 / `../llm-learning/` (resume at Lesson 2: local model with Ollama)
- CCA Foundations prep and registration
- Books, CS221, Dive into Deep Learning, deep-learning crash courses
- Academy modules and the prompt-engineering notebooks
- Sprint-tracker app enhancements

**After Milestone 1:** sprint Day 5 — tool use. Don't open it until then.
