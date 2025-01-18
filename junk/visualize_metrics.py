import numpy as np
import matplotlib.pyplot as plt

from graph_library.metrics import *
from junk.utils import set_configuration


metrics = {
    'cosine similarity': cosine_similatiry,
    'reversed cosine similarity': reversed_cosine_similarity,
    'Kulback-Leibler divergence': kulback_leibler,
    'reversed Kulback-Leibler divergence': reversed_kulback_leibler
}

for metric_name in metrics:
    plt.clf()
    metric = metrics.get(metric_name)

    for actor_meaning in (0.1, 0.25, 0.5, 0.75, 0.9):
        x = list(np.linspace(0., 1, 100))
        y = [
            metric([v, 1 - v], [actor_meaning, 1 - actor_meaning])
            for v in x
        ]

        plt.plot(x, y, label=f'$m([x, 1 - x], [{actor_meaning:.2f}, {(1 - actor_meaning):.2f}]$', linewidth=3)

    plt.axhline(0, -10, 10, color='black', linewidth=3)
    plt.axvline(0, -1, 1, color='black', linewidth=3)
    set_configuration('actor origin value', 'metric value', big_legend=False)
    plt.title(metric_name)
    plt.savefig(f'./plots/metrics/{metric_name.replace(" ", "_")}.png')
