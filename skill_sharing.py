from test_data import graph, islands
from island import Island

def compute_priority(island, alpha=0.5, beta=1.0):
    return alpha * island.population + beta * island.last_visited

def greedy_skill_sharing_route(start, graph, islands, alpha=0.5, beta=1.0):
    current = start
    route = [current]
    islands[current].visited = True

    for _ in range(len(islands) - 1):
        neighbors = graph.get(current, {})
        best_score = -1
        next_island = None

        for neighbor in neighbors:
            if not islands[neighbor].visited:
                score = compute_priority(islands[neighbor], alpha, beta)
                if score > best_score:
                    best_score = score
                    next_island = neighbor

        if next_island is None:
            break  # No more reachable unvisited islands

        current = next_island
        islands[current].visited = True
        route.append(current)

        # Update last_visited for all unvisited islands
        for name, island in islands.items():
            if not island.visited:
                island.last_visited += 1
            else:
                island.last_visited = 0

    return route

# For testing/debugging only
if __name__ == "__main__":
    route = greedy_skill_sharing_route('Hawaii', graph, islands)
    print("Leader Route:", route)
