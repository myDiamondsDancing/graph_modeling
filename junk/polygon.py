from pathlib import Path

import copy
import random

from graph_library import Graph
from graph_library.visualization import *
from graph_library.metrics import *

from junk.utils import dialog



def get_mean_opinion(graph):

    def callback(node_info: dict) -> float:
        return node_info.get('meaning')[0]

    return np.mean(graph.node_map(callback))


metrics = {
    'cosine similarity': cosine_similatiry,
    'reversed cosine similarity': reversed_cosine_similarity,
    'Kulback-Leibler divergence': kulback_leibler,
    'reversed Kulback-Leibler divergence': reversed_kulback_leibler,
    None: None
}


def modeling(graph: Graph, epochs: int = 100, metric: Optional[Callable] = None, changing_factor: float = 1e-3):
    graph = copy.copy(graph)

    for epoch in range(epochs):
        edges_data = graph.edges(include_data=True)
        nodes_data = graph.nodes(include_data=True)

        for u, v in edges_data:

            actor1 = nodes_data[u].get('opinion')
            actor2 = nodes_data[v].get('opinion')

            if metric is not None:
                metric_value = metric(actor1, actor2)
            else:
                metric_value = 0.5

            if random.random() < metric_value:
                actor1, actor2 = dialog(actor1[0], actor2[1], changing_factor=changing_factor)

                graph.modify_node(u, opinion=[actor1, 1 - actor1])
                graph.modify_node(v, opinion=[actor2, 1 - actor2])

    return graph


graph = Graph.from_polynomial(100, .1)
visualize(graph, to_file=f'plots/modeling/origin_{get_mean_opinion(graph):.4f}_mo.png')

for metric_name in metrics:
    metric = metrics.get(metric_name)

    for changing_factor in (1e-3, 1e-2, 0.05, 0.1):
        for epochs in (10, 25, 50, 75, 100, 250, 500):
            graph_after_modeling = modeling(graph, epochs, metric=metric)

            if metric_name is None:
                metric_name = "random"

            filepath = Path(f'./plots/modeling/{metric_name.replace(" ", "_")}')

            if not filepath.exists():
                filepath.mkdir()

            filepath = filepath / str(changing_factor)

            if not filepath.exists():
                filepath.mkdir()

            visualize(
                graph_after_modeling,
                to_file=filepath / f'{epochs}_epochs_cf_{get_mean_opinion(graph_after_modeling):.4f}_mo.png'
            )
