# 📚 Paper Reading Log

Track and visualize your paper reading with auto-updated charts.

<!--CHART_START-->
![By category](assets/category_stylish.svg)

![Activity heatmap](assets/activity_heatmap.svg)


**Breakdown**

| Category | Count |
|---|---|
| LLM | 37 |
| Multimodal (T/S) | 27 |
| TTS | 23 |
| NAC | 12 |
| ML | 6 |
| ASR | 5 |
| Dataset (Speech) | 4 |
| Multimodal (T/I) | 4 |
| Speech | 4 |
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
| **Total** | **137** |

**Recently read**

- [ExGRPO: Learning to Reason from Experience](https://arxiv.org/abs/2510.02245) — *LLM* (2025-10-06)
- [Knapsack RL: Unlocking Exploration of LLMs via Optimizing Budget Allocation](https://arxiv.org/abs/2509.25849) — *LLM* (2025-10-03)
- [Sora 2 System Card](https://cdn.openai.com/pdf/50d5973c-c4ff-4c2d-986f-c72b5d0ff069/sora_2_system_card.pdf) — *Multimodal Generation* (2025-10-01)
- [SPADE: Structured Pruning and Adaptive Distillation for Efficient LLM-TTS](https://arxiv.org/abs/2509.20802) — *TTS* (2025-09-30)
- [ShinkaEvolve: Towards Open-Ended And Sample-Efficient Program Evolution](https://arxiv.org/abs/2509.19349) — *ML* (2025-09-29)
- [Building Tailored Speech Recognizers for Japanese Speaking Assessment](https://arxiv.org/abs/2509.20655) — *ASR* (2025-09-28)
- [Qwen3-Omni Technical Report](https://arxiv.org/abs/2509.17765) — *Multimodal (T/S/I/V)* (2025-09-27)
- [VoXtream: Full-Stream Text-to-Speech with Extremely Low Latency](https://www.arxiv.org/abs/2509.15969) — *TTS* (2025-09-26)
- [Language Models Resist Alignment: Evidence From Data Compression](https://aclanthology.org/2025.acl-long.1141.pdf) — *LLM* (2025-09-25)
- [Sidon: Fast and Robust Open-Source Multilingual Speech Restoration for Large-scale Dataset Cleansing](https://arxiv.org/abs/2509.17052) — *Speech* (2025-09-24)
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
