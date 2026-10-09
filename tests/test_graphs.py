import networkx as nx

from knight_queens.enumerate import solutions
from knight_queens.graphs import count_isomorphism_classes, induced_knight_graph
from knight_queens.metrics import statistics


def test_graph_edges_match_metric():
    for p in solutions(8):
        assert induced_knight_graph(p).number_of_edges() == statistics(p)["e"]


def test_induced_graphs_are_bipartite():
    for n in range(1, 9):
        for p in solutions(n):
            assert nx.is_bipartite(induced_knight_graph(p))


def test_exact_isomorphism_classes():
    graphs = [
        nx.path_graph(3),
        nx.Graph([(10, 11), (11, 12)]),
        nx.complete_graph(3),
    ]
    assert count_isomorphism_classes(graphs) == 2
