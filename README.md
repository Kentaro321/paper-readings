# 📚 Paper Reading Log

Track and visualize your paper reading with auto-updated charts.

<!--CHART_START-->
![By category](assets/category_stylish.svg)

![Activity heatmap](assets/activity_heatmap.svg)


**Breakdown**

| Category | Count |
|---|---|
| LLM | 45 |
| Multimodal (T/S) | 40 |
| TTS | 25 |
| NAC | 14 |
| Speech | 8 |
| ML | 7 |
| ASR | 6 |
| Multimodal (T/I) | 6 |
| Dataset (Speech) | 5 |
| Multimodal (T/S/I/V) | 4 |
| Multimodal (T/S/I) | 2 |
| ST | 2 |
| VC | 2 |
| Audio | 1 |
| Image | 1 |
| Multimodal Generation | 1 |
| NV | 1 |
| Text Embedding | 1 |
| THG | 1 |
| TTI | 1 |
| **Total** | **173** |

**Recently read**

- [Learning Dynamics of LLM Finetuning](https://openreview.net/pdf?id=tPNHOoZFl9) — *LLM* (2025-11-12)
- [Safety Alignment Should be Made More Than Just a Few Tokens Deep](https://openreview.net/pdf?id=6Mxhg9PtDE) — *LLM* (2025-11-10)
- [OpenOmni: Advancing Open-Source Omnimodal Large Language Models with Progressive Multimodal Alignment and Real-Time Self-Aware Emotional Speech Synthesis](https://arxiv.org/abs/2501.04561) — *Multimodal (T/S/I)* (2025-11-09)
- [MULTI-Bench: A Multi-Turn Interactive Benchmark for Assessing Emotional Intelligence ability of Spoken Dialogue Models](https://arxiv.org/abs/2511.00850) — *Speech* (2025-11-08)
- [FillerSpeech: Towards Human-Like Text-to-Speech Synthesis with Filler Insertion and Filler Style Control](https://aclanthology.org/2025.emnlp-main.1730.pdf) — *TTS* (2025-11-07)
- [VITA-1.5: Towards GPT-4o Level Real-Time Vision and Speech Interaction](https://arxiv.org/abs/2501.01957) — *Multimodal (T/S/I/V)* (2025-11-06)
- [FLEXI: Benchmarking Full-duplex Human-LLM Speech Interaction](https://arxiv.org/abs/2509.22243) — *Multimodal (T/S)* (2025-11-05)
- [Efficient and Direct Duplex Modeling for Speech-to-Speech Language Model](https://www.isca-archive.org/interspeech_2025/hu25f_interspeech.pdf) — *Multimodal (T/S)* (2025-11-04)
- [POWSM: A Phonetic Open Whisper-Style Speech Foundation Model](https://www.arxiv.org/abs/2510.24992) — *ASR* (2025-11-03)
- [Aligning Spoken Dialogue Models from User Interactions](https://arxiv.org/abs/2506.21463) — *Multimodal (T/S)* (2025-11-01)
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
