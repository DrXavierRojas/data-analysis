import numpy as np
import matplotlib.pyplot as plt

plt.style.use("styles/minimal.mplstyle")

x = np.linspace(0, 10, 500)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(4, 3))
ax.plot(x, y)
ax.set_xlabel("x")
ax.set_ylabel("sin(x)")
fig.tight_layout()
fig.savefig("figures_dev/fig1_sinewave.pdf")
