# Research Project Template — Tutorial

This project is structured to support the full data workflow: from acquisition, to analysis, to paper publication.

---

## 📁 Folder Structure Overview

### Top-Level: `my-project-name/`

| Folder | Description |
|--------|-------------|
| `data/raw/` | Unmodified raw datasets (e.g., CSVs from measurement instruments) |
| `data/processed/` | Cleaned and prepared datasets for analysis |
| `data/metadata/` | YAML/JSON logs for experimental conditions |
| `analysis/` | Jupyter notebooks or exploratory Python scripts |
| `interactive/` | Plotly-based scripts for rapid data exploration |
| `plots/` | Development scripts for figures (not final) |
| `figures_dev/` | Output files from draft figures |
| `utils/` | General-purpose Python helpers |
| `styles/` | Matplotlib `.mplstyle` files for visual consistency |
| `papers/` | Subfolders for finalized publications |

---

### Inside: `papers/my-paper-title/`

| Folder | Description |
|--------|-------------|
| `data/` | Frozen, publication-ready datasets |
| `plots/` | Scripts to generate each paper figure |
| `figures/` | Final `.pdf` and `.png` figures |
| `styles/` | Style file used for figures in the paper |
| `paper/` | LaTeX manuscript files |

---

## 📦 Dependency Management

### Option A: Using `pip` (recommended for light, local workflows)

Create a virtual environment and install:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Option B: Using `conda` (recommended for cross-platform or larger projects)

```bash
conda env create -f environment.yml
conda activate my-project-env
```

---

## 🧪 Suggested Workflow

1. Place raw data in `data/raw/`
2. Write a script in `utils/processing.py` to clean/process data → save to `data/processed/`
3. Explore trends in `analysis/` or `interactive/`
4. Draft figure scripts in `plots/` → output to `figures_dev/`
5. Once finalized, migrate data and scripts into a new `papers/my-paper-title/` folder

---

## 🧠 Student Guidelines

- Every result must be reproducible from a script.
- Use LaTeX labels, vector output (`.pdf`), and high DPI for publication plots.
- Write clear docstrings/comments for all reusable functions.
- Document your experiments and analysis history in `README.md` or Markdown logs.

---

## ✅ Example Commands

```bash
# run a figure script
python plots/dev_fig_phase_diagram.py

# launch notebook
jupyter notebook analysis/explore_phase_diagram.ipynb
```

---


---

## 🗃️ Data and Metadata: How They're Connected

Every raw or processed dataset should be accompanied by a metadata file that describes:
- Experimental/simulation parameters
- Sample conditions or configurations
- Software version and random seeds
- Researcher notes and context

### 👇 Example

- Raw data: `data/raw/helium_run_2025-04-17.csv`
- Metadata: `data/metadata/helium_run_2025-04-17.yaml`

These files **share a naming convention** so scripts and researchers can associate them automatically.

In Python, you might write:

```python
import pandas as pd
import yaml

data = pd.read_csv("data/raw/helium_run_2025-04-17.csv")
with open("data/metadata/helium_run_2025-04-17.yaml", "r") as f:
    meta = yaml.safe_load(f)

print(f"Temperature: {meta['conditions']['temperature_mK']} mK")
```

---

Using metadata ensures that:
- Your figures are interpretable even years later
- Students understand what parameters produced each result
- Papers are reproducible and data is traceable

---
