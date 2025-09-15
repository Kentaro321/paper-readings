# 📚 Paper Reading Log

Track and visualize your paper reading with auto-updated charts.

<!--CHART_START-->
![By category](assets/category_stylish.svg)

![Activity heatmap](assets/activity_heatmap.svg)


**Breakdown**

| Category | Count |
|---|---|
| LLM | 30 |
| Multimodal (T/S) | 25 |
| TTS | 21 |
| NAC | 12 |
| ML | 5 |
| ASR | 4 |
| Dataset (Speech) | 4 |
| Multimodal (T/I) | 3 |
| Speech | 3 |
| Multimodal (T/S/I/V) | 2 |
| ST | 2 |
| VC | 2 |
| Audio | 1 |
| Multimodal (T/S/I) | 1 |
| Text Embedding | 1 |
| THG | 1 |
| TTI | 1 |
| **Total** | **118** |

**Recently read**

- [Defeating Nondeterminism in LLM Inference](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/) — *LLM* (2025-09-15)
- [Simplifying, Stabilizing and Scaling Continuous-Time Consistency Models](https://arxiv.org/abs/2410.11081) — *ML* (2025-09-14)
- [EchoX: Towards Mitigating Acoustic-Semantic Gap via Echo Training for Speech-to-Speech LLMs](https://www.arxiv.org/abs/2509.09174) — *Multimodal (T/S)* (2025-09-13)
- [Leveraging Unit Language Guidance to Advance Speech Modeling in Textless Speech-to-Speech Translation](https://aclanthology.org/2025.findings-acl.75.pdf) — *ST* (2025-09-13)
- [Soundwave: Less is More for Speech-Text Alignment in LLMs](https://aclanthology.org/2025.acl-long.917.pdf) — *Multimodal (T/S)* (2025-09-13)
- [Continuous Audio Language Models](https://www.arxiv.org/abs/2509.06926) — *Multimodal (T/S)* (2025-09-11)
- [Step-Audio 2 Technical Report](https://arxiv.org/abs/2507.16632) — *Multimodal (T/S)* (2025-09-10)
- [AudioBench: A Universal Benchmark for Audio Large Language Models](https://aclanthology.org/2025.naacl-long.218v2.pdf) — *Multimodal (T/S)* (2025-09-09)
- [Koel-TTS: Enhancing LLM based Speech Generation with Preference Alignment and Classifier Free Guidance](https://arxiv.org/abs/2502.05236) — *TTS* (2025-09-08)
- [NanoCodec: Towards High-Quality Ultra Fast Speech LLM Inference](https://arxiv.org/abs/2508.05835) — *NAC* (2025-09-08)
<!--CHART_END-->

## How to add a new paper

Add paper info to `data/papers.yml` in the following format:

```yaml
- title: "Your paper title"
  category: "LLM"
  date: "YYYY-MM-DD"
  link: "https://..."
```

## Reuse This Repo

- Use as template: Click "Use this template" on GitHub, then edit `data/papers.yml`.
- Timezone: Set `PAPERS_TZ` in the workflow (default `Asia/Tokyo`).
- CI validation: The workflow validates `data/papers.yml` before building charts.
- Export: CI also writes a machine-readable `data/papers.json` for reuse.

See `TEMPLATE.md` for details.

## Development

With `uv` (recommended):

```
uv sync
uv run scripts/validate_papers.py
uv run scripts/build_readme.py
uv run scripts/export_json.py
```

## License

- Code: MIT (`LICENSE`)
- Content (notes, `data/papers.yml`, generated charts in `assets/`): CC BY 4.0 — https://creativecommons.org/licenses/by/4.0/
