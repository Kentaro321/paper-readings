# 📚 Paper Reading Log

Track and visualize your paper reading with auto-updated charts.

<!--CHART_START-->
![By category](assets/category_stylish.svg)

![Activity heatmap](assets/activity_heatmap.svg)


**Breakdown**

| Category | Count |
|---|---|
| LLM | 29 |
| Multimodal (T/S) | 21 |
| TTS | 21 |
| NAC | 12 |
| ASR | 4 |
| Dataset (Speech) | 4 |
| ML | 4 |
| Multimodal (T/I) | 3 |
| Speech | 3 |
| Multimodal (T/S/I/V) | 2 |
| VC | 2 |
| Audio | 1 |
| Multimodal (T/S/I) | 1 |
| ST | 1 |
| Text Embedding | 1 |
| THG | 1 |
| TTI | 1 |
| **Total** | **111** |

**Recently read**

- [AudioBench: A Universal Benchmark for Audio Large Language Models](https://aclanthology.org/2025.naacl-long.218v2.pdf) — *Multimodal (T/S)* (2025-09-09)
- [Koel-TTS: Enhancing LLM based Speech Generation with Preference Alignment and Classifier Free Guidance](https://arxiv.org/abs/2502.05236) — *TTS* (2025-09-08)
- [NanoCodec: Towards High-Quality Ultra Fast Speech LLM Inference](https://arxiv.org/abs/2508.05835) — *NAC* (2025-09-08)
- [LLM-Enhanced Dialogue Management for Full-Duplex Spoken Dialogue Systems](https://arxiv.org/abs/2502.14145) — *Multimodal (T/S)* (2025-09-07)
- [Reinforcement Learning Enhanced Full-Duplex Spoken Dialogue Language Models for Conversational Interactions](https://openreview.net/pdf?id=QbLbXz8Idp) — *Multimodal (T/S)* (2025-09-07)
- [MixedG2P-T5: G2P-free Speech Synthesis for Mixed-script texts using Speech Self-Supervised Learning and Language Model](https://www.arxiv.org/abs/2509.01391) — *TTS* (2025-09-07)
- [Failing Forward: Improving Generative Error Correction for ASR with Synthetic Data and Retrieval Augmentation](https://aclanthology.org/2025.findings-acl.125.pdf) — *ASR* (2025-09-06)
- [Generative Annotation for ASR Named Entity Correction](https://www.arxiv.org/abs/2508.20700) — *ASR* (2025-09-05)
- [CLEAR: Continuous Latent Autoregressive Modeling for High-quality and Low-latency Speech Synthesis](https://arxiv.org/abs/2508.19098) — *TTS* (2025-09-04)
- [SpectroStream: A Versatile Neural Codec for General Audio](https://arxiv.org/abs/2508.05207) — *NAC* (2025-09-03)
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
