# 🧾 Metadata Guide

Well-structured metadata makes your experiments and simulations reproducible.

## 📄 YAML Metadata

Stored in `data/metadata/`:
```yaml
experiment:
  id: run-0425
  operator: Xavier
  temperature_mK: 35.2
```

Load in Python:

```python
import yaml
with open("data/metadata/run-0425.yaml") as f:
    meta = yaml.safe_load(f)
```

## 📁 Naming Convention

Match metadata and data files by name:
- `raw/helium_run_0425.csv`
- `metadata/helium_run_0425.yaml`

## 🔄 Simulation Metadata (JSON)

Stored config example:
```json
{
  "grid_points": 1024,
  "potential": "harmonic",
  "seed": 1337
}
```
