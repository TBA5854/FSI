import numpy as np
import random
import fsi
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

ul = 0.1
ur = 0.1
u = 1.0
n_points = 10000


def make_heights():
    h1 = random.uniform(0, 5)

    diffs = [
        random.uniform(0.1, 5.0),  # d12 (h2 - h1 >= 0.1)
        random.uniform(0.0, 5.0),  # d23 (h3 - h2 >= 0)
        random.uniform(0.1, 5.0),  # d34 (h4 - h3 >= 0.1)
        random.uniform(0.0, 5.0),  # d45 (h5 - h4 >= 0)
        random.uniform(0.1, 5.0),  # d56 (h6 - h5 >= 0.1)
    ]

    for i in range(len(diffs)):
        if random.random() < 0.4:
            diffs[i] *= random.uniform(0.4, 0.9)
        else:
            diffs[i] *= random.uniform(1.0, 1.8)

    d12, d23, d34, d45, d56 = diffs
    h2 = h1 + d12
    h3 = h2 + d23
    h4 = h3 + d34
    h5 = h4 + d45
    h6 = h5 + d56

    print(f"h1={h1:.3f}, d12={d12:.3f}, d23={d23:.3f}, d34={d34:.3f}, d45={d45:.3f}, d56={d56:.3f}")
    return h1, h2, h3, h4, h5, h6


def compute_curve(heights):
    h1, h2, h3, h4, h5, h6 = heights
    x = np.linspace(0, h6 + h1, n_points)
    f = [fsi.hexagonal_fuzzer((h1, h2, h3, h4, h5, h6), ul, ur, u, xi) for xi in x]
    return x, np.array(f)


def plot_on_ax(ax, heights):
    ax.clear()
    x, f = compute_curve(heights)
    h1, h2, h3, h4, h5, h6 = heights

    ax.plot(x, f, label="fsi")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_title(
        f"Hexagonal FSI: h1={h1:.2f}, h2={h2:.2f}, h3={h3:.2f}, h4={h4:.2f}, h5={h5:.2f}, h6={h6:.2f}"
    )

    y_max = max(f.max(), ul, ur, u)
    ax.set_xlim(0, x[-1])
    ax.set_ylim(0, y_max * 1.05)

    for idx, (hx, color) in enumerate(
        zip([h1, h2, h3, h4, h5, h6], ["red", "magenta", "cyan", "brown", "olive", "green"])
    ):
        ax.axvline(hx, color=color, linestyle="--", alpha=0.5)
        ax.text(hx, ax.get_ylim()[1], f"h{idx+1}", color=color, ha="center", va="bottom", fontsize=8, fontweight="bold")

    for val, color, name in zip([ul, ur, u], ["orange", "purple", "blue"], ["ul", "ur", "u"]):
        ax.text(ax.get_xlim()[1], val, name, color=color, va="center", ha="right", fontsize=8, fontweight="bold")

    ax.axhline(ur, color="purple", linestyle="--", label="ur")
    ax.axhline(ul, color="orange", linestyle="--", label="ul")
    ax.axhline(u, color="blue", linestyle="--", label="u")

    ax.legend()
    ax.grid(True)


# build figure + button
fig, ax = plt.subplots(figsize=(9, 4))
plt.subplots_adjust(bottom=0.18)  # make space for the button

current_heights = make_heights()
plot_on_ax(ax, current_heights)

button_ax = fig.add_axes([0.81, 0.03, 0.12, 0.05])
rerun_button = Button(button_ax, "Rerun")

def on_rerun(event):
    new_heights = make_heights()
    plot_on_ax(ax, new_heights)
    fig.canvas.draw_idle()


rerun_button.on_clicked(on_rerun)

plt.show()
