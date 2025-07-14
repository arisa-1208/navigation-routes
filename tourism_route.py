import heapq
from island import Island
from test_data import islands, graph as graph_data

# -------------------------------
# Graph Class
# -------------------------------

class Graph:
    def __init__(self):
        self.islands = {}
        self.routes = {}

    def add_island(self, island):
        self.islands[island.name] = island
        if island.name not in self.routes:
            self.routes[island.name] = []

    def add_route(self, from_id, to_id, travel_time):
        if from_id in self.islands and to_id in self.islands:
            self.routes[from_id].append((to_id, travel_time))

    def get_neighbors(self, island_id):
        return self.routes.get(island_id, [])

# -------------------------------
# Modified Dijkstra's Algorithm
# -------------------------------

def find_best_route(graph, start_id, max_time=float('inf')):
    if start_id not in graph.islands:
        print("Start island not found")
        return {}

    pq = [(0, start_id, set(), [start_id])]
    best = {}
    best_result = {'time': float('inf'), 'path': [], 'experiences': set()}

    while pq:
        curr_time, curr_id, seen, path = heapq.heappop(pq)
        island = graph.islands[curr_id]
        new_exps = set()
        extra_time = 0

        for exp in island.experiences:
            if exp['name'] not in seen:
                new_exps.add(exp['name'])
                extra_time += exp['time']

        total_time = curr_time + extra_time
        updated_seen = seen | new_exps

        if (len(updated_seen) > len(best_result['experiences']) or
            (len(updated_seen) == len(best_result['experiences']) and total_time < best_result['time'])):
            if total_time <= max_time:
                best_result['time'] = total_time
                best_result['path'] = path[:]
                best_result['experiences'] = updated_seen.copy()

        for neighbor_id, t in graph.get_neighbors(curr_id):
            next_time = total_time + t
            state = (neighbor_id, frozenset(updated_seen))

            if next_time <= max_time and (state not in best or next_time < best[state]):
                best[state] = next_time
                heapq.heappush(pq, (next_time, neighbor_id, updated_seen.copy(), path + [neighbor_id]))

    if best_result['experiences']:
        return {
            'total_time': f"{best_result['time']} hours",
            'path': best_result['path'],
            'experiences_count': len(best_result['experiences']),
            'unique_experiences': list(best_result['experiences'])
        }
    else:
        return {}

# -------------------------------
# Convert Shared Data to Graph
# -------------------------------

def convert_to_graph(graph_dict, island_dict):
    g = Graph()
    for island in island_dict.values():
        g.add_island(island)
    for src, neighbors in graph_dict.items():
        for dest, time in neighbors.items():
            g.add_route(src, dest, time)
    return g

# -- Wrapper for external import --
def tourism_route(graph, start_id, max_time=float('inf')):
    return find_best_route(graph, start_id, max_time)

# ----------------
#    Test Cases
# ----------------

if __name__ == "__main__":
    g = convert_to_graph(graph_data, islands)

    print("--- Tourist from Hawaii (No Time Limit) ---")
    result1 = find_best_route(g, "Hawaii")
    if result1:
        print("Total Time:", result1['total_time'])
        print("Path:", " → ".join(result1['path']))
        print("Experiences Count:", result1['experiences_count'])
        print("Unique Experiences:", ", ".join(result1['unique_experiences']))
    else:
        print("No good route found")

    print("\n--- Tourist from Tahiti (Max 300 Hours) ---")
    result2 = find_best_route(g, "Tahiti", max_time=300)
    if result2:
        print("Total Time:", result2['total_time'])
        print("Path:", " → ".join(result2['path']))
        print("Experiences Count:", result2['experiences_count'])
        print("Unique Experiences:", ", ".join(result2['unique_experiences']))
    else:
        print("No good route found within the time limit")

    print("\n--- Tourist from Rapanui (Max 100 Hours) ---")
    result3 = find_best_route(g, "Rapanui", max_time=100)
    if result3:
        print("Total Time:", result3['total_time'])
        print("Path:", " → ".join(result3['path']))
        print("Experiences Count:", result3['experiences_count'])
        print("Unique Experiences:", ", ".join(result3['unique_experiences']))
    else:
        print("No good route found within the time limit")
