import heapq
from island import Island
from test_data import islands, graph

def dijkstra_tree(islands_dict, graph, source_name):
    island_list = list(islands_dict.values())
    name_to_index = {island.name: idx for idx, island in enumerate(island_list)}
    n = len(island_list)

    dist = [float('inf')] * n
    parent = [-1] * n
    visited = [False] * n

    src = name_to_index[source_name]
    dist[src] = 0
    pq = [(0, src)]

    while pq:
        d, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True

        u_name = island_list[u].name
        for v_name, weight in graph.get(u_name, {}).items():
            v = name_to_index[v_name]
            if not visited[v] and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                parent[v] = u
                heapq.heappush(pq, (dist[v], v))

    # Output sorted tree
    print(f"Shortest-Path Tree from {source_name}:")
    print(f"{source_name} is the root (distance 0)")

    tree_edges = []
    for i in range(n):
        if i != src and parent[i] != -1:
            tree_edges.append((dist[i], f"{island_list[parent[i]].name} -> {island_list[i].name} (distance {dist[i]})"))

    tree_edges.sort()
    for _, line in tree_edges:
        print(line)
