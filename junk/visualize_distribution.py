import numpy as np
import matplotlib.pyplot as plt

from graph_library import Graph
from junk.utils import set_configuration


for probability in (0.1, 0.25, 0.5, 0.75, 0.9):
    nodes = np.arange(50, 1000, 1)
    y = [len(Graph.from_polynomial(node, probability).edges()) for node in nodes]

    plt.plot(nodes, y, label=f'p = {probability}')
    set_configuration('number of nodes', 'number of edges')
    plt.savefig('./plots/graph_nodes/nodes.png')