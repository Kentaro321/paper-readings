# 📚 Paper Reading Log

Track and visualize your paper reading with auto-updated charts.

<!--CHART_START-->
![By category](assets/category_stylish.svg)

![Activity heatmap](assets/activity_heatmap.svg)


**Breakdown**

| Category | Count |
|---|---|
| LLM | 35 |
| Multimodal (T/S) | 27 |
| TTS | 21 |
| NAC | 12 |
| ML | 5 |
| ASR | 4 |
| Dataset (Speech) | 4 |
| Multimodal (T/I) | 4 |
| Speech | 4 |
| Multimodal (T/S/I/V) | 2 |
| ST | 2 |
| VC | 2 |
| Audio | 1 |
| Image | 1 |
| Multimodal (T/S/I) | 1 |
| NV | 1 |
| Text Embedding | 1 |
| THG | 1 |
| TTI | 1 |
| **Total** | **129** |

**Recently read**

- [Language Models Resist Alignment: Evidence From Data Compression](https://aclanthology.org/2025.acl-long.1141.pdf) — *LLM* (2025-09-25)
- [Sidon: Fast and Robust Open-Source Multilingual Speech Restoration for Large-scale Dataset Cleansing](https://arxiv.org/abs/2509.17052) — *Speech* (2025-09-24)
- [Llama-Mimi: Speech Language Models with Interleaved Semantic and Acoustic Tokens](https://arxiv.org/abs/2509.14882) — *Multimodal (T/S)* (2025-09-23)
- [Fairness through Difference Awareness: Measuring Desired Group Discrimination in LLMs](https://aclanthology.org/2025.acl-long.341.pdf) — *LLM* (2025-09-23)
- [A Theory of Response Sampling in LLMs: Part Descriptive and Part Prescriptive](https://aclanthology.org/2025.acl-long.1454.pdf) — *LLM* (2025-09-22)
- [Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention](https://aclanthology.org/2025.acl-long.1126.pdf) — *LLM* (2025-09-21)
- [MiMo-Audio: Audio Language Models are Few-Shot Learners](https://github.com/XiaomiMiMo/MiMo-Audio/blob/main/MiMo-Audio-Technical-Report.pdf) — *Multimodal (T/S)* (2025-09-20)
- [LLM-I: LLMs are Naturally Interleaved Multimodal Creators](https://arxiv.org/abs/2509.13642) — *Multimodal (T/I)* (2025-09-19)
- [WaveFM: A High-Fidelity and Efficient Vocoder Based on Flow Matching](https://arxiv.org/abs/2503.16689) — *NV* (2025-09-18)
- [Single-stream Policy Optimization](https://arxiv.org/abs/2509.13232) — *LLM* (2025-09-17)
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
