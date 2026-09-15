# llm-learning

Working repo for **Track 1 — LLM Substrate**: building substrate-level understanding of how LLMs actually work.

The goal is to get enough footing to interrogate a vendor claim or an architecture proposal instead of following its shape.

**Not** in scope: implementing transformers, training models, PyTorch, classical data science. If an exercise starts asking for a training loop, it's the wrong target.

- [`Track1_LLM_Substrate_Lesson_Plan.md`](Track1_LLM_Substrate_Lesson_Plan.md) — the full 9-lesson plan (0–8), resources, and checkpoints
- [`SOURCES.md`](SOURCES.md) — registry of every external resource, with status and last-verified dates
- [`notes.md`](notes.md) — the durable output: hand-written synthesis across all lessons

**Start with Lesson 0** — 30 minutes of reading that gives you the layer model everything else hangs on.

---

## Prerequisites

Things that live outside this repo and won't come with a clone:

- **Python 3.11+**
- **Ollama** — needed from Lesson 2 onward. Install natively, not in Docker (containers on macOS have no Metal/GPU access, so you'd be stuck on slow CPU-only inference):
```bash
  curl -fsSL https://ollama.com/install.sh | sh
```
  Or download the `.dmg` from https://ollama.com/download

---

## Getting started

```bash
git clone <repo-url> llm-learning
cd llm-learning

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Verify:

```bash
python -c "import tiktoken; print(tiktoken.get_encoding('cl100k_base').encode('hello'))"
ollama --version
```

Launch notebooks:

```bash
jupyter lab
```

---

## Layout
```
notes.md                      the durable output — hand-written synthesis
Track1_..._Lesson_Plan.md     the full plan: lessons, resources, checkpoints
requirements.txt              direct dependencies

01-tokenizer/                 notebook — tokenizer behavior
02-local-model/               shell + Ollama, not Python
03-transformer-reading/       reading notes (course, videos)
04-context/                   notebook — context window, KV cache
05-rag/                       notebook + a source doc long enough to chunk badly
06-training-lifecycle/        reading only
07-cost-model/                spreadsheet — beats code for this
08-consolidate/               synthesis
```

Lesson directories are created as they're reached — missing ones just mean not started.

---

## Two conventions worth keeping

**Hands-on before reading, every time.** There's no existing mental scaffold for LLM internals, so the exercises build the scaffold and the reading attaches to it. Reverse the order and the reading slides off. Each lesson in the plan is sequenced this way deliberately.

**[`notes.md`](notes.md) is the real output — write it by hand.** Not the checkboxes, not the notebooks. Notebooks are the working log: observations sit inline, directly under the output that provoked them. `notes.md` is the design doc: conclusions, corrected assumptions, things worth explaining to someone else. It's the one artifact here that's unambiguously your own thinking, and that's the point of it. Don't generate it.

---

## Notebook gotcha

Out-of-order cell execution produces results you can't reproduce. **Restart-and-run-all before trusting any observation.**

---

## Disk

Ollama models are the space cost, and they live in `~/.ollama/models`, not here:

- 3B quantized ≈ 2 GB
- 8B ≈ 5 GB
- 34B ≈ 19 GB

`ollama list` to see what's installed, `ollama rm <name>` to clear what you're done comparing.