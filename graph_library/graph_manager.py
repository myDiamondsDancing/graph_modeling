import pickle
import random
from typing import (
    Dict,
    List,
    Any,
    Tuple,
    Type,
    Union
)

import numpy as np
import networkx as nx

from .utils import expand

NodesInfo: Type = Dict[int, Dict[str, Any]]
EdgesInfo: Type = Dict[Tuple[int, int], Dict[str, Any]]


class Graph:
    def __init__(self):

        # create graph matrix
        self._edges: np.ndarray = np.zeros((0, 0)).astype(np.uint8)

        # create info lists
        self._n: int = 0
        self._nodes_info: NodesInfo = dict()
        self._edges_info: EdgesInfo = dict()

    def add_node(self, **kwargs) -> 'Graph':

        # expand graph matrix to size (n + 1, n + 1)
        self._edges: np.ndarray = expand(self._edges)
        self._nodes_info[self._n] = kwargs.copy()
        self._n += 1

        return self

    def add_edge(self, start: int, end: int, **kwargs) -> 'Graph':

        # update graph matrix
        self._edges[start][end] = 1
        self._edges[end][start] = 1
        self._edges_info[(start, end)] = kwargs.copy()

        return self

    def modify_node(self, node: int, **kwargs) -> None:
        self._nodes_info[node].update(kwargs)

    def modify_edge(self, edge: tuple, **kwargs) -> None:
        self._edges_info[edge].update(kwargs)

    def nodes(self, include_data: bool = False) -> Union[NodesInfo, List[int]]:
        if include_data:
            return {i: self._nodes_info[i] for i in range(self._n)}
        else:
            return list(range(self._n))

    def edges(self, include_data: bool = False) -> Union[EdgesInfo, List[Tuple[int, int]]]:
        if include_data:
            return self._edges_info.copy()
        else:
            return list(self._edges_info.keys())

    def is_reachable(self, start: int, end: int) -> bool:
        return self._edges[start][end] == 1

    def neighbours(self, node: int) -> List[int]:
        return list(np.arange(self._n)[self._edges[node] == 1])

    @staticmethod
    def from_file(filepath: str) -> 'Graph':
        with open(filepath, 'rb') as graph_file:
            graph_info: Dict[str, Any] = pickle.load(graph_file)

        graph: 'Graph' = Graph()

        for node_info in graph_info['nodes_info']:
            graph.add_node(**node_info)

        for (start, end), edge_info in graph_info['edges_info'].items():
            graph.add_edge(start, end, **edge_info)

        return graph

    def save(self, filepath: str) -> None:
        with open(filepath, 'wb') as graph_file:
            graph_info: Dict[str, Any] = {
                'nodes_info': self._nodes_info,
                'edges_info': self._edges_info,
            }

            pickle.dump(graph_info, graph_file)

    @staticmethod
    def from_polynomial(num_nodes: int, edge_prob: float = .5) -> 'Graph':
        graph = Graph()

        for i in range(num_nodes):
            value = random.random()
            graph.add_node(
                name=f'actor_{i}',
                meaning=[value, 1 - value]
            )

        for u in range(num_nodes - 1):
            for v in range(u + 1, num_nodes):
                rand_val = random.uniform(0, 1)
                if rand_val < edge_prob:
                    graph.add_edge(u, v)

        return graph


    def to_networkx_graph(self) -> nx.Graph:
        graph_repr: nx.Graph = nx.Graph()

        for n in self._nodes_info:
            graph_repr.add_node(n, **self._nodes_info[n])

        for e in self._edges_info:
            graph_repr.add_edge(*e, **self._edges_info[e])

        return graph_repr


    def node_map(self, callback: callable):
        return [callback(node_data) for node_data in self._nodes_info.values()]




