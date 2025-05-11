import matplotlib.pyplot as plt

def setup_figure(context="paper", figsize=(3.3, 2.5)):
    if context == "paper":
        plt.style.use("papers/my-paper-title/styles/paper.mplstyle")
    else:
        plt.style.use("styles/draft.mplstyle")
    fig, ax = plt.subplots(figsize=figsize)
    return fig, ax
