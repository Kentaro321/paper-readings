# 📚 Paper Reading Log

Track and visualize your paper reading with auto-updated charts.

<!--CHART_START-->
![By category](assets/category_stylish.svg)

![Activity heatmap](assets/activity_heatmap.svg)


**Breakdown**

| Category | Count |
|---|---|
| LLM | 43 |
| Multimodal (T/S) | 39 |
| TTS | 24 |
| NAC | 14 |
| ML | 7 |
| Speech | 7 |
| ASR | 6 |
| Multimodal (T/I) | 6 |
| Dataset (Speech) | 5 |
| Multimodal (T/S/I/V) | 3 |
| ST | 2 |
| VC | 2 |
| Audio | 1 |
| Image | 1 |
| Multimodal (T/S/I) | 1 |
| Multimodal Generation | 1 |
| NV | 1 |
| Text Embedding | 1 |
| THG | 1 |
| TTI | 1 |
| **Total** | **166** |

**Recently read**

- [Efficient and Direct Duplex Modeling for Speech-to-Speech Language Model](https://www.isca-archive.org/interspeech_2025/hu25f_interspeech.pdf) — *Multimodal (T/S)* (2025-11-04)
- [POWSM: A Phonetic Open Whisper-Style Speech Foundation Model](https://www.arxiv.org/abs/2510.24992) — *ASR* (2025-11-03)
- [Aligning Spoken Dialogue Models from User Interactions](https://arxiv.org/abs/2506.21463) — *Multimodal (T/S)* (2025-11-01)
- [Contrastive Preference Optimization: Pushing the Boundaries of LLM Performance in Machine Translation](https://arxiv.org/abs/2401.08417) — *LLM* (2025-10-31)
- [Can Speech LLMs Think while Listening?](https://arxiv.org/abs/2510.07497) — *Multimodal (T/S)* (2025-10-30)
- [Understanding the Repeat Curse in Large Language Models from a Feature Perspective](https://aclanthology.org/2025.findings-acl.406.pdf) — *LLM* (2025-10-29)
- [Slot Filling as a Reasoning Task for SpeechLLMs](https://arxiv.org/abs/2510.19326) — *Multimodal (T/S)* (2025-10-28)
- [Audio Flamingo 3: Advancing Audio Intelligence with Fully Open Large Audio Language Models](https://arxiv.org/abs/2507.08128) — *Multimodal (T/S)* (2025-10-27)
- [Scaling Speech-Text Pre-training with Synthetic Interleaved Data](https://arxiv.org/abs/2411.17607) — *Multimodal (T/S)* (2025-10-26)
- [SAC: Neural Speech Codec with Semantic-Acoustic Dual-Stream Quantization](https://www.arxiv.org/abs/2510.16841) — *NAC* (2025-10-25)
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
