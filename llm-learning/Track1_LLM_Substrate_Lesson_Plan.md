# Track 1 — LLM Substrate: Lesson Plan

## The goal
ML equivalent of “I use AWS but don’t understand VPCs.” Substrate understanding, not model-building. Enough footing to interrogate a vendor claim or an architecture proposal instead of following its shape.

## Total scope
20–30 hours, 9 lessons (0–8). No deadline. Do a lesson, stop, come back whenever.

## Design principle
Hands-on first, reading second. You have no existing scaffold for LLM internals, so the exercises build the scaffold and the reading attaches to it. Reverse the order and the reading slides off.

## Not in scope
Implementing transformers, training models, PyTorch, classical data science. If a resource starts asking you to write a training loop, you’ve drifted.

## Source of truth
Every external link is registered in `SOURCES.md` / `SOURCES.md` with status and last-verified date.

## Where this sits in the AI-engineering stack

Chip Huyen’s three-layer model is a cleaner map than “learn AI.” Any AI-application stack has three layers, and you start at the top and move down only as needed:

| Layer | What it covers | This track |
|---|---|---|
| Application development | Prompts, context, evaluation, interfaces | Track 2 (eval) and Track 3 (orchestration) |
| Model development | Modeling, training, fine-tuning, inference optimization, dataset engineering | Track 1 — substrate understanding only, no tooling |
| Infrastructure | Model serving, compute/data management, monitoring | Skipped entirely |

Track 1 is deliberately the “understanding” of the model-development layer without the practice of it. Huyen makes this distinction explicitly: ML knowledge is no longer a prerequisite for building AI applications — she’s met successful builders with no interest in gradient descent — but it stays valuable because it widens the set of tools available to you and helps when a model misbehaves. That’s exactly the line this track draws.

The other framing worth carrying: AI engineering is less about “model development” and more about **adaptation** and **evaluation**. Adaptation splits by whether you change or prompt-based techniques (no weight change) vs. fine-tuning (weight change). Keep that fork in mind through Lesson 6.

---

# Lesson 0 — The Map

## 30 min — Reading only

Read this before Lesson 1. It’s Chapter 1 of the *AI Engineering* book, published free, and it gives you the vocabulary and the layer model to hang everything else on.

- [ ] **The AI Engineering Stack** — free excerpt, *AI Engineering*  
  `https://newsletter.pragmaticengineer.com/p/the-ai-engineering-stack`

## What to take from it

- [ ] The three-layer stack above — know which layer you’re at in any moment.
- [ ] AI engineering vs. ML engineering: less modeling, more adaptation and evaluation.
- [ ] Why evaluation is harder with foundation models: open-ended outputs mean no exhaustive ground truth to compare against, unlike close-ended tasks like fraud detection.
- [ ] The “same model” example — the same model scored 83.7% or 80.4% on the same benchmark depending purely on prompt technique. **That’s your first argument for why eval design is a real skill.**

> Don’t read the rest of the book yet. Lesson 8.

## Setup (once, ~10 min)

```bash
mkdir -p ~/dev/ai-engineer/llm-learning && cd ~/dev/ai-engineer/llm-learning
python3 -m venv .venv
source .venv/bin/activate
pip install tiktoken transformers sentence-transformers numpy jupyterlab
```

### Install Ollama natively
**(not Docker — no Metal/GPU access in containers on Mac, so you’d be stuck on CPU-only inference).**

```bash
curl -fsSL [https://ollama.com/install.sh](https://ollama.com/install.sh) | sh
```

Or download the `.dmg` manually from <https://ollama.com/download> — same thing, more conventional on a managed Mac.

Verify:

```bash
ollama --version
```

Useful commands later:

```bash
ollama list              # what’s installed
ollama rm <name>         # free space
ollama stop <name>       # stop the service
```

> ⚠️ **On a work machine:** macOS may prompt for admin rights. If Cox endpoint management blocks it, that’s an IT conversation, not something to work around — and it’s a legitimate ask given this is platform evaluation work.

Directory structure — one directory per lesson, uniformly. `notes.md` at root as the single cross-lesson artifact.

```
~/dev/ai-engineer/llm-learning/
├── .venv/
├── notes.md                         # ← THE DURABLE OUTPUT
├── 01-tokenizer/
│   └── tokenizer.ipynb              # create then run
├── 02-local-model/
│   ├── observations.md              # shell + Ollama, not Python
│   └── memory-usage.md              # screenshots
├── 03-transformer-reading/
│   └── notes                         # from course/videos
├── 04-context/
│   └── context.ipynb                # notebook
├── 05-rag/
│   ├── rag.ipynb                    # notebook
│   └── source-doc.txt               # something of yours, long enough to chunk badly
├── 06-training-lifecycle/
│   └── reading-only/
├── 07-cost-model/
│   └── cost-model.xlsx              # spreadsheet beats code here
└── 08-consolidate/
```

### Notebooks vs. notes — the split that matters

**Notebooks = observation layer.** Lessons 1, 4, and 5 are tweak-and-rerun by nature: change a string, see the token list; change chunk size, watch retrieval break. Put observations inline, directly under the output that provoked them. “Capitalization changes the token” is far more useful three inches below the token list than described later from memory.

notes.md = synthesis layer. Conclusions, corrected assumptions, things you’d explain to someone else. This is what you re-read in a year. Hunting through notebooks for your own conclusions is worse than opening one markdown file.

*In familiar terms: the notebook is the working log, `notes.md` is the design doc. Same reason architecture decisions don’t live in a Jira comment thread.*

**Two practical cautions:**
- Notebook hidden state (out-of-order execution → results you can’t reproduce) is a real hazard. **Restart-and-run-all before trusting any observation.**
- Notebooks are JSON and diff badly in Git. Another reason to keep `notes.md` separate if you want version history.

**Notebooks only cover 3 of the 9 lessons.** Lessons 0 and 6 are reading-only. Lesson 2 is shell + Ollama. Lesson 7 is cost math — use a spreadsheet.

> ➡️ **Write `notes.md` by hand.** Don’t generate it. It’s the one artifact in this track that’s unambiguously your own thinking, and that’s the whole point of it.

Disk note: the Ollama app itself is ~300MB. Models are the real cost — 3B quantized ~2GB, 8B ~5GB, 34B ~19GB. Watch `~/.ollama/models/`, and `ollama rm` what you’re done comparing.

---

# Lesson 1 — Tokenization
### ~45–60 min. Hands-on first, no reading

**Do this before reading anything.**

```python
import tiktoken

enc = tiktoken.get_encoding("cl100k_base")

for s in [
    "Hello",                            # baseline
    "hello",                            # capitalization = different token
    " hello",                           # leading space = different token
    "Delayable",                        # uncommon name → fragments
    "unbelievable",                     # common word, many whole
    "café",                             # accented char
    "🔥",                               # emoji
    "SELECT Id FROM Account WHERE CreatedDate = TODAY",  # SOQL/code
    "நன்றி",                         # Tamil for “thank you”; see note below
]:
    print(f"{s!r:50} {enc.encode(s)}")
```

> **Why the Tamil word is in there:** `cl100k_base` and most production tokenizers were trained on a corpus that's overwhelmingly English, so the vocabulary contains whole English words as single tokens but has almost no Tamil sub-word units. Tamil text therefore falls back to near-byte-level encoding — often **several tokens per character**, versus roughly 0.75 tokens per word for English. "நன்றி" is five characters and one word, and it can cost as many tokens as a short English sentence.
>
> This is the fastest way to *see* that per-token pricing is not language-neutral. The same effect hits Hindi, Arabic, Thai, and CJK scripts. The practical consequences: a non-English feature can cost several times more per request than its English equivalent, it consumes the context window far faster, and it hits token limits on inputs that look short. If a Cox product ever serves non-English users, that's a real cost and capacity line item — not a rounding error.
>
> The SOQL line makes a smaller version of the same point: code tokenizes less efficiently than prose because identifiers, punctuation, and casing patterns fragment.

**A follow-on worth running** — the cost gradient isn't English-vs-everything-else, it tracks training-corpus representation:

```python
for s in ["thank you", "gracias", "danke", "谢谢", "شكرا", "நன்றி"]:
    print(f"{s!r:15} {len(enc.encode(s)):3} tokens {enc.encode(s)}")
```

**Observe and write down in notes.md:**
- [ ] Capitalization changes the token
- [ ] A leading space changes the token
- [ ] Your own name fragments into several pieces
- [ ] Emoji costs multiple tokens
- [ ] Non-English costs more per character — but on a *gradient*, not a cliff
- [ ] SOQL/Apex tokenizes differently than prose

**Then sit with what falls out:** why per-token pricing doesn't track word count; why non-English and code cost more; why some prompts behave oddly at invisible boundaries.

**Read after (optional, ~20 min):**
- Hugging Face LLM Course, **Chapter 6** (tokenizers, down to byte-pair encoding) — https://huggingface.co/learn/llm-course/chapter6/1

**Checkpoint:** Can I explain to a PM why a Tamil-language feature costs 3× more per request than the English one?

---

# Lesson 2 — Run a Model Locally
### ~1 hr · The single highest-value exercise in the track

This is your VPC-by-hand equivalent. Do not skip it.

```bash
ollama pull llama3.2:3b
```

**Before you prompt it:**
- [ ] Find the file on disk (`~/.ollama/models`). Look at its size.
- [ ] Pull a second quantization or a different size (`ollama pull llama3.2:1b`). Compare sizes.
- [ ] Run `ollama run llama3.2:3b` and watch memory usage while it generates (Activity Monitor / `htop`)
- [ ] Notice the delay before the first token vs. the speed of subsequent tokens *(this is prefill vs. decode — Lesson 4)*

**Write in notes.md:** what changed about how you think about "the model" now that it's a file with a size.

**Read after (~15 min):**
- Interactive explainer: https://hammadabbasi.com/under-the-hood/how-llms-work — draggable embedding-space visualization
- https://www.knovo.dev/guides/how-llms-work — opens with the warning that treating an LLM as a magic box leads to poor cost/reliability/evaluation decisions

**Checkpoint:** "The model" is no longer a service. It's a file with a memory cost and a speed/quality tradeoff.

---

# Lesson 3 — Transformer Architecture & Inference Path
### ~3-4 hrs · Now the real reading

You've seen tokens behave and watched a model consume memory. The concepts now have somewhere to attach.

**Primary (do this one):**
- [ ] **DeepLearning.AI — "How Transformer LLMs Work"** (free, short) — https://www.deeplearning.ai/courses/how-transformer-llms-work
  - Jay Alammar & Maarten Grootendorst. Transformer components + tokenization strategy comparison. Exactly the right altitude.

**Visual intuition (pick one, ~1 hr):**
- [ ] **3Blue1Brown** — transformer/attention chapters on YouTube. Best visual explanation of attention available anywhere.
- [ ] **Andrej Karpathy** — his ~1hr "Intro to LLMs" overview talk (conceptual). ⚠️ **Not** the build-from-scratch series — wrong target.

**Supplementary reading:**
- [ ] Hugging Face LLM Course, **Chapters 1–2** — transformer architecture, what happens behind the `pipeline()` abstraction — https://huggingface.co/learn/llm-course/chapter1/1

**Checkpoint:** Can I trace the path from input text to output text, naming what happens at each stage?

---

# Lesson 4 — Context Window Mechanics & KV Cache
### ~2 hrs · Where the architectural decisions live

This is the lesson that most changes how you design systems. Context management is an architectural decision, not a config value — this is where you find out why.

**Hands-on first (~30 min):**
- [ ] Feed the local model a short prompt, then a very long one. Time both.
- [ ] Notice where the time goes: long prompt = slow first token (prefill), then normal generation speed (decode)
- [ ] Try a long document + a question at the very end vs. the very beginning. Compare answer quality.

**The number that makes this concrete:** foundation models are autoregressive — tokens generate sequentially. At 10ms per token, a 100-token output takes a full second. Typical internet applications are built around ~100ms expectations. That gap is why inference optimization became its own subfield, and why autoregressive generation is an *architectural constraint*, not a performance detail you tune later.

**Read:**
- [ ] **LLM Inference in 2026: How It Works, Latency & Cost** — https://futureagi.com/blog/llm-inference-human-prompts-2025/
  - *Prefill vs. decode is the single most useful mechanical concept in this whole track.*
- [ ] **The LLM Inference Roadmap** (Sept 2026) — https://martinuke0.github.io/posts/2026-09-02-the-llm-inference-roadmap-i-wish-more-engineers-followed/
  - Written for working engineers, not inference specialists. Good on why KV cache dominates memory at long context.

> ⚠️ **Caveat:** most current KV-cache writing targets *inference/serving engineers* — GPU memory hierarchy, vLLM vs. TensorRT-LLM, tuning `gpu-memory-utilization`. That's operating a data center when you wanted to understand VPCs. **Read for concepts, not to act on.** If you find yourself comparing serving frameworks, stop.

  - Written for working engineers, not inference specialists. Good on why KV cache dominates memory at long context.

> ⚠️ **Caveat:** most current KV-cache writing targets *inference/serving engineers* — GPU memory hierarchy, vLLM vs. TensorRT-LLM, tuning `gpu-memory-utilization`. That's operating a data center when you wanted to understand VPCs. **Read for concepts, not to act on.** If you find yourself comparing serving frameworks, stop.

**Checkpoint:** Can I explain why stuffing more context into a prompt isn't free, in both cost and quality terms?

---

# Lesson 5 — Embeddings, Retrieval & Failure Modes
### ~3 hrs · Build it by hand, then break it

**Build (~1.5 hrs) — no framework, ~20 lines:**

```python
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

# 1. chunk a document (start naive — fixed character count)
# 2. embed each chunk
# 3. embed a query
# 4. cosine similarity, return top-k
```

Use one of your own documents — something long enough to chunk badly.

**Then deliberately break it and record what happens:**
- [ ] Chunk mid-sentence. Watch retrieval degrade.
- [ ] Chunk so a key fact splits across two chunks. Watch it become unretrievable.
- [ ] Write a query that's semantically close but factually wrong ("what's the refund policy" against a doc about returns). Watch it confidently retrieve the wrong thing.
- [ ] Query with a term that appears nowhere in the source but means the same thing. See whether it works.

This is where "why did it surface the wrong context" becomes something you've *seen* rather than read about.

**Read after:**
- [ ] **Maxime Labonne's LLM Course** — embeddings and retriever sections — https://huggingface.co/blog/mlabonne/llm-course
  - Use as a *map*. Read the retrieval sections, skip the rest.

**Checkpoint:** Given a RAG system producing bad answers, can I name four distinct places the failure could be and how to distinguish them?

---

# Lesson 6 — Training Lifecycle
### ~2 hrs · Reading only

The lesson that lets you evaluate claims instead of accepting them. When someone says "the model was trained on X" or "we fine-tuned it on our data," this is what tells you what that actually means.

**Read:**
- [ ] **Maxime Labonne's LLM Course** — pretraining / SFT / post-training sections — https://huggingface.co/blog/mlabonne/llm-course
- [ ] **Hugging Face LLM Course, Chapters 3-4** — read for *what fine-tuning changes*, not to run the code — https://huggingface.co/learn/llm-course/chapter3/1

**The distinction to nail down** — write your own one-paragraph answer to each in notes.md:
- [ ] What does **pretraining** produce? (Weights start random. For LLMs it's usually text completion. It's ~98% of total compute for a model like InstructGPT — which is why only a handful of organizations do it.)
- [ ] What does **supervised fine-tuning** change vs. pretraining? (Continues from existing weights, so far fewer resources.)
- [ ] What does **post-training / RLHF** change vs. SFT?
- [ ] Mechanically, what does **fine-tuning** modify that **RAG** does not? And vice versa?
- [ ] When is **prompting** sufficient and when is it structurally incapable of solving the problem?

> **Terminology trap worth knowing.** *Post-training* and *fine-tuning* describe conceptually the same operation — the word choice signals **who did it**. It's post-training when the model developer does it before release (e.g. making a model better at following instructions); it's fine-tuning when you do it to adapt a released model to your needs.
>
> Separately: people routinely misuse **"training"** to mean prompt engineering — "I trained ChatGPT on my journal entries." Colloquially reasonable, technically wrong: feeding context into the input is prompt engineering, not training. Training always changes weights. **You will now catch this in vendor conversations**, and it's a fast read on whether someone actually knows what they're selling.

**Checkpoint:** A vendor says "our model is fine-tuned on automotive data." Can I ask three questions that would reveal whether that's meaningful?

---

# Lesson 7 — Serving Economics & Model Selection
### ~2 hrs · The build-vs-buy layer

Directly relevant to decisions you make today.

**Read:**
- [ ] **AI Hero — "5 Questions To Ask Before Choosing An LLM"** (free) — https://www.aihero.dev/how-to-choose-an-llm
  - Open vs. closed models, cost, latency, hosting options. Short and practical.
- [ ] **LLM Inference: From Tokens to Answers** — https://www.turingpost.com/p/llm-inference-from-tokens-to-answers
  - Why "the model generates the next token" stops being a sufficient mental model once orchestration, retrieval, memory and tool calls are involved.

**Hands-on:**
- [ ] Price out a real scenario with actual numbers — take a Cox-shaped workload (e.g. summarizing N call transcripts/day at M tokens each) and compute API cost vs. self-hosted cost
- [ ] Note where the crossover is, and what assumptions move it

**Checkpoint:** Can I build the cost model for an AI feature without asking a vendor to do it for me?

---

# Lesson 8 — Consolidate
### ~4-6 hrs · Systems-level synthesis

By now the pieces exist. This lesson connects them at the altitude you actually work at.

- [ ] **"AI Engineering"** — Chip Huyen
  - Repeatedly named 2026's top pick. Systems-level, written for people building AI products and AI architects. **The most job-relevant thing in this track** — read it *last*, when you have the substrate to evaluate it rather than take it on faith.
  - You already read Ch. 1 in Lesson 0. Chapters worth prioritizing: 2 (foundation models, sampling), 3 (evaluation methodology), 5-6 (prompt engineering, context construction), 7-9 (inference optimization).
- [ ] **"Hands-On Large Language Models"** — Alammar & Grootendorst *(optional, if you want a visual reference to keep)*
  - Same authors as the Lesson 3 course. Heavily visual, understanding-oriented.

**❌ Still skip:** "Build a Large Language Model from Scratch" (Raschka). Excellent book, wrong target — builds a transformer in PyTorch with no shortcuts. That's capability building.

**Final checkpoint — the real test:**
- [ ] Review your own notes.md. What did you believe at Lesson 1 that you'd now correct?
- [ ] Pick a real decision at Cox involving AI (Bedrock config, a vendor claim, an Agentforce capability question). Can you now interrogate it rather than defer?

---

## Sources

All external links in this plan are registered in [`SOURCES.md`](SOURCES.md) with status and last-verified date. **When a link dies, update `SOURCES.md` first**, then fix it here. Dead entries stay in the registry rather than getting deleted — knowing what *was* the reference is useful.

Two entries there are flagged as unverified (the YouTube series) and one as higher link-rot risk (a personal blog). Check those first if something looks stale.

---

## Reference Table — What Each Lesson Closes

| Lesson | AWS equivalent | Closes |
|---|---|---|
| 0 — The map | Reading the architecture diagram before touching anything | Vocabulary, layer model, why eval is hard |
| 1 — Tokenization | Understanding packets | Why cost ≠ word count |
| 2 — Local model | Standing up your own instance | Model as artifact, not service |
| 3 — Architecture | How traffic flows through a VPC | The inference path end to end |
| 4 — Context/KV cache | Instance sizing, why it costs what it costs | Context as architecture, not config |
| 5 — Retrieval | Debugging a network path | Where RAG actually fails |
| 6 — Training lifecycle | Build/deploy pipeline | Evaluating "trained on X" claims |
| 7 — Serving economics | Managed vs. self-hosted | Build-vs-buy with real numbers |
| 8 — Consolidate | Architecture review | Systems-level judgment |

---

## Loose Rules

- **Hands-on before reading, every time.** The exercises build the scaffold. Lesson 0 is the one exception — it's a map, and 30 minutes of orientation saves more than it costs.
- **notes.md is the actual output.** Not completion. "What surprised me" is what you'll still have in a year.
- If a resource starts asking you to write a training loop — **wrong target, back out.**
- Lessons 1 and 2 together are under two hours and close more of the gap than a full course. If you do nothing else, do those.