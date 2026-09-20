# Sources

Registry for every external resource referenced in this repo. The lesson plan keeps inline clickable links for readability; **this file is where link health is tracked.**

**Convention:** when a link dies or gets superseded, update it *here* first with a note, then fix the lesson plan. Keep dead entries rather than deleting them — knowing something *was* the reference is useful.

**Status key:** ✅ verified · ⚠️ moved/changed · ❌ dead · 💰 paid/gated

Last full sweep: 2026-09-13

---

## Courses

| ID | Title | For | URL | Status |
|---|---|---|---|---|
| C1 | DeepLearning.AI — How Transformer LLMs Work | Lesson 3 · **primary course for this track** | https://www.deeplearning.ai/courses/how-transformer-llms-work | ✅ free |
| C2 | Hugging Face LLM Course | Lessons 1, 3, 6 — Ch. 1–4, 6 only | https://huggingface.co/learn/llm-course/chapter1/1 | ✅ free |
| C3 | LinkedIn Learning — Generative AI: Introduction to LLMs | Optional orientation | (search LinkedIn Learning) | ✅ - |
| C4 | LinkedIn Learning — Generative AI: Working with LLMs | Optional orientation | (search LinkedIn Learning) | ✅ - |

## Books

| ID | Title | Author | For | Status |
|---|---|---|---|---|
| B1 | AI Engineering | Chip Huyen | Lesson 8 · **most job-relevant item in the track** | 💰 O'Reilly |
| B2 | Hands-On Large Language Models | Alammar & Grootendorst | Lesson 8, optional visual reference | 💰 |
| B3 | ~~Build a Large Language Model from Scratch~~ | Raschka | ❌ **DELIBERATELY EXCLUDED** — builds a transformer in PyTorch. Excellent book, wrong target. | — |

## Articles & explainers

| ID | Title | For | URL | Status |
|---|---|---|---|---|
| A1 | The AI Engineering Stack (Ch. 1 of B1, free excerpt) | **Lesson 0** — read first as orienting map | https://newsletter.pragmaticengineer.com/p/the-ai-engineering-stack | ✅ free |
| A2 | Under the Hood: How LLMs Work | Lesson 2 — interactive embedding-space viz | https://hammadabbasi.com/under-the-hood/how-llms-work | ✅ |
| A3 | How LLMs Work (for builders) | Lesson 2 | https://www.knovo.dev/guides/how-llms-work | ✅ |
| A4 | LLM Inference in 2026: How It Works, Latency & Cost | Lesson 4 — prefill vs. decode | https://futureagi.com/blog/llm-inference-human-prompts-2025/ | ✅ |
| A5 | The LLM Inference Roadmap | Lesson 4 — KV cache at engineer altitude | https://martinuke0.github.io/posts/2026-09-02-the-llm-inference-roadmap-i-wish-more-engineers-followed/ | ✅ personal blog — **higher link-rot risk** |
| A6 | LLM Inference: From Tokens to Answers | Lesson 7 | https://www.turingpost.com/p/llm-inference-from-tokens-to-answers | ✅ |
| A7 | The LLM Course (curated roadmap) | Lessons 5, 6 — use as a *map*, not a syllabus | https://huggingface.co/blog/mlabonne/llm-course | ✅ free |
| A8 | AI Hero — 5 Questions Before Choosing an LLM | Lesson 7 | https://www.aihero.dev/how-to-choose-an-llm | ✅ free |

## Video

| ID | Title | For | Status |
|---|---|---|---|
| V1 | 3Blue1Brown — transformer/attention chapters | Lesson 3 — best visual intuition on attention | ⚠️ not directly verified |
| V2 | Andrej Karpathy — "Intro to LLMs" (~1hr overview talk) | Lesson 3 — conceptual. **Not** the build-from-scratch series. | ⚠️ not directly verified |

## Tools

| ID | Tool | For | URL |
|---|---|---|---|
| T1 | Ollama | Lesson 2 onward | https://ollama.com/download |
| T2 | tiktoken | Lesson 1 | pip |
| T3 | sentence-transformers | Lesson 5 | pip |

---

## Other tracks (not Track 1 — parked here so the links don't get lost)

| Track | Resource | URL |
|---|---|---|
| 2 — Evaluation | Hamel Husain's LLM Evals guide | https://hamel.dev/blog/posts/evals-faq/ |
| 2 — Evaluation | AI Evals for Engineers & PMs (self-paced) | https://courseflix.net/course/ai-evals-for-engineers-pms |
| 2 — Evaluation | AI Evals for Engineers & PMs (cohort) | https://maven.com/parlance-labs/evals |
| 2 — Evaluation | Evidently AI — free 7-day email course | https://www.evidentlyai.com/llm-evaluations-course |
| 2 — Evaluation | LLM Evals in 2026: A Practical Guide | https://devtoollab.com/blog/llm-evals-guide-2026 |
| 2 — Evaluation | Community evals study guide | https://github.com/ombharatiya/ai-system-design-guide/blob/main/ai_evals_comprehensive_study_guide.md |
| 2/3 | AI Hero — AI Engineer Roadmap (lessons 4–7 only) | https://www.aihero.dev/ai-engineer-roadmap |
| 3 — Agentic | AI Hero — Model Context Protocol tutorial | https://www.aihero.dev/model-context-protocol-tutorial |
| 3 — Agentic | Build an MCP Client and Server from Scratch Using Python (Zahere, Apr 2025) | https://zahere.com/build-an-mcp-client-and-server-from-scratch-using-python |
| 3 — Agentic | FastAPI MCP SSE Server with JWT Auth & Custom Client (Zahere, May 2025) | https://zahere.com/fastapi-mcp-sse-server-with-jwt-auth-and-custom-client |
| 3 — Agentic | Google "Agents" white paper deep dive (Zahere, Jan 2025) | https://zahere.com/a-deep-dive-into-googles-agents-white-paper-hype-or-revolution |

---

## Track 2 note — eval sets are data work

Building a real eval set is substantially data work: assembling, cleaning, labelling. The old "data scientists spend 80-90% of their time cleaning data" claim is less central for LLM application work than it was for classical ML, but it resurfaces here. Budget for it — eval datasets don't assemble themselves.

---

## Reviewed and rejected

Kept so the decision doesn't get re-litigated.

| Resource | Why not |
|---|---|
| Deep Learning Crash Course (No Starch) | Good book. Teaches building models — CNNs, GANs, diffusion. Wrong layer. |
| Build a Large Language Model from Scratch (Raschka) | Same: PyTorch transformer implementation. Capability building, not substrate. |
| [How I Transitioned Into an 'AI Engineer'](https://zahere.com/how-i-transitioned-into-an-ai-engineer) (Zahere, Feb 2024) | Validating but not additive, and dated — resource list is pre-agentic (LangChain app courses, prompt-engineering shorts), no eval content. Its useful parts (scope to your actual use cases; math isn't the gate) are already reflected in the plan. His *newer* MCP/agent posts are the valuable part of that site — listed above. |
| Educative — Become a Machine Learning Engineer | Capability building. Wrong target. |

### Intro-tier GenAI material (reviewed 2026-09)

A set of links from around 2023 — plausibly early GenAI onboarding or E&Y-era orientation. All at or below Lesson 0 level. Recorded here so the list doesn't resurface.

| Resource | Why not |
|---|---|
| [Introduction to Generative AI](https://www.youtube.com/watch?v=G2fqAlgmoPo) (Google Cloud, Dr. Gwendolyn Stripling) | Introductory microlearning — define GenAI, explain how it works, describe model types and applications. ~1 hr. First-day orientation for someone who's never touched this. |
| [Introduction to Large Language Models](https://www.youtube.com/watch?v=zizonToFXDs) (Google Cloud) | Same series, same tier. |
| [Generative AI Fundamentals](https://www.youtube.com/watch?v=1fQ1DDMmiqo) | Same tier. |
| [Introducing Generative AI Suite by Observe.AI](https://www.youtube.com/watch?v=lAxpDfy2WHo) | Vendor product marketing, not a learning resource. *Only possible use: competitive intel on contact-centre AI — relevant to Genesys work, not to this track.* |
| [Make flowchart with GPT](https://www.youtube.com/watch?v=TklABBggj1w) | Tooling tip. Unrelated to anything in the plan. |
| [What are LLMs, and how are they used in GenAI?](https://www.computerworld.com/article/3697649/what-are-large-language-models-and-how-are-they-used-in-generative-ai.html) (Computerworld) | General-press explainer, written for business readers. |
| [Generative adversarial network](https://en.wikipedia.org/wiki/Generative_adversarial_network) (Wikipedia) | **Actively off-target.** GANs are a pre-LLM image/data-generation architecture — the deep-learning-build layer this track excludes. Wouldn't inform any decision about LLM systems. |

**The pattern to notice:** the gap isn't "what is generative AI" — that was answered by shipping call summarization in 2023/24. The gap is tokenization mechanics, KV cache, retrieval failure modes. Intro-tier material re-answers a question already closed.