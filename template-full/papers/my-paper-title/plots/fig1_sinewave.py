import numpy as np
import matplotlib.pyplot as plt
from utils.plotting import setup_figure

# Generate deterministic clean data
x = np.linspace(0, 10, 500)
y = np.sin(x)

fig, ax = setup_figure(context="paper", figsize=(3.3, 2.5))
ax.plot(x, y, label=r"$\sin(x)$", color="tab:blue")
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$f(x)$")
ax.legend()
fig.tight_layout()
fig.savefig("papers/my-paper-title/figures/fig1_sinewave.pdf")
