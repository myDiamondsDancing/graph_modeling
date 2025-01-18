import matplotlib.pyplot as plt
import numpy as np

from junk.utils import dialog, set_configuration


for actor_meaning in (0.1, 0.25, 0.5, 0.75, 0.9):
    x = list(np.linspace(0., 1, 100))
    y = [dialog(v, actor_meaning)[0] for v in x]

    plt.clf()
    plt.plot(x, y, label=f'$d(x, {actor_meaning})$\n$\epsilon = 0.5$', linewidth=3)
    plt.axhline(0, -10, 10, color='black', linewidth=3)
    plt.axvline(0, -1, 1, color='black', linewidth=3)
    plt.grid(True)
    set_configuration('actor origin value', 'actor new value')
    plt.savefig(f'./plots/dialog/dialog_with_{actor_meaning}.png')


for actor_meaning in (0.1, 0.25, 0.5, 0.75, 0.9):
    x = list(np.linspace(0., 1, 100))
    y = [dialog(v, actor_meaning)[0] for v in x]

    plt.plot(x, y, label=f'$d(x, {actor_meaning})$\n$u = 0.5$', linewidth=3)
    plt.axhline(0, -10, 10, color='black', linewidth=3)
    plt.axvline(0, -1, 1, color='black', linewidth=3)
    plt.grid(True)
    set_configuration('actor origin value', 'actor new value', big_legend=False)


plt.savefig(f'./plots/dialog/dialog_full.png')