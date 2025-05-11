#!/usr/bin/env python3
import os
from pathlib import Path
import shutil

TEMPLATE_FOLDERS = [
    "data/raw",
    "data/processed",
    "data/metadata",
    "analysis",
    "interactive",
    "plots",
    "figures_dev",
    "utils",
    "styles",
    "papers"
]

def create_project(name):
    base = Path(name)
    for folder in TEMPLATE_FOLDERS:
        path = base / folder
        path.mkdir(parents=True, exist_ok=True)
    with open(base / "README.md", "w") as f:
        f.write(f"# {name}\n\nGenerated with `init_project.py`.")
    print(f"Project '{name}' created successfully.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python init_project.py MyProjectName")
    else:
        create_project(sys.argv[1])
