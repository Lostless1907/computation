import argparse
import networkx as nx


def board_knight_graph(n: int) -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from((r, c) for r in range(n) for c in range(n))
    moves = (
        (1, 2), (1, -2), (-1, 2), (-1, -2),
        (2, 1), (2, -1), (-2, 1), (-2, -1),
    )

    for r in range(n):
        for c in range(n):
            for dr, dc in moves:
                rr, cc = r + dr, c + dc
                if 0 <= rr < n and 0 <= cc < n:
                    graph.add_edge((r, c), (rr, cc))

    return graph


def count_four_vertex_paths(graph: nx.Graph) -> int:
    degree = dict(graph.degree())
    return sum(
        (degree[u] - 1) * (degree[v] - 1)
        for u, v in graph.edges()
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=12)
    args = parser.parse_args()

    for n in range(1, args.max_n + 1):
        graph = board_knight_graph(n)
        print(n, graph.number_of_edges(), count_four_vertex_paths(graph))


if __name__ == "__main__":
    main()
