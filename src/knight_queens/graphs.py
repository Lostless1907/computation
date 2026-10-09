import networkx as nx

from knight_queens.metrics import knight_edge_pairs


def induced_knight_graph(p: tuple[int, ...] | list[int]) -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(range(len(p)))
    graph.add_edges_from(knight_edge_pairs(p))
    return graph


def graph_summary(graph: nx.Graph) -> dict[str, int | bool]:
    return {
        "vertices": graph.number_of_nodes(),
        "edges": graph.number_of_edges(),
        "components": nx.number_connected_components(graph),
        "triangles": sum(nx.triangles(graph).values()) // 3,
        "bipartite": nx.is_bipartite(graph),
    }


def count_isomorphism_classes(graphs: list[nx.Graph]) -> int:
    buckets: dict[str, list[nx.Graph]] = {}

    for graph in graphs:
        key = nx.weisfeiler_lehman_graph_hash(graph)
        bucket = buckets.setdefault(key, [])
        if not any(nx.is_isomorphic(graph, old) for old in bucket):
            bucket.append(graph.copy())

    return sum(map(len, buckets.values()))
