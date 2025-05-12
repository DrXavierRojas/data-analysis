# 📈 Plotting Guide

This page explains how plotting is structured in both templates and how to create high-quality, reproducible figures.

## ✍️ File Naming

Use clear and meaningful names:
- `fig1_entropy_scaling.py`
- `plot_powerlaw_fit.py`

## 📊 Tools

- **Matplotlib**: for paper-ready figures (`.pdf`)
- **Plotly**: for interactive plots in notebooks or dashboards

## 🧰 Reuse Styles

Each template includes `.mplstyle` files in `styles/`.

To use a style:

```python
import matplotlib.pyplot as plt
plt.style.use("styles/minimal.mplstyle")
```

## 📤 Output Format

- Always export paper figures as `.pdf`
- Drafts or presentations can use `.png` or `.svg`
