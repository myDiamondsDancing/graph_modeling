from typing import *

import matplotlib.pyplot as plt
import networkx as nx

from .graph_manager import Graph


def visualize(graph: Graph, with_opinion: bool = True, with_labels: bool = False, to_file: Optional[str] = None, title: str = '') -> None:
    nx_graph: nx.Graph = graph.to_networkx_graph()

    if with_opinion:
        colors = [info.get('meaning')[0] for n, info in nx_graph.nodes(data=True)]
        colors = [(c, c, c) for c in colors]
    else:
        colors = ['blue' for i in range(len(nx_graph.nodes))]

    fig = plt.figure(figsize=(15, 10))
    pos = nx.spring_layout(nx_graph, seed=1)
    nx.draw(nx_graph, pos=pos, with_labels=with_labels, node_color=colors, edge_color=(0.5, 0.5, 0.5))
    plt.title(title)
    plt.xticks([], [])
    plt.yticks([], [])
    fig.set_facecolor('lightblue')

    if to_file is not None:
        plt.savefig(to_file)
