import pandas as pd
import numpy as np
from utils.plotting import setup_figure

# Simulate some data for plotting
x = np.linspace(0, 10, 500)
y = np.sin(x) + 0.1 * np.random.randn(500)

fig, ax = setup_figure(context="draft", figsize=(6, 4))
ax.plot(x, y, label="sin(x) + noise")
ax.set_xlabel("x")
ax.set_ylabel("Amplitude")
ax.set_title("Draft Sine Wave")
ax.legend()
fig.tight_layout()
fig.savefig("figures_dev/fig_draft_sinewave.pdf")
