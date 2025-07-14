from island import Island
from test_data import islands, graph as graph_data
from skill_sharing import greedy_skill_sharing_route
from resource_distribution import dijkstra_tree
from tourism_route import find_best_route, convert_to_graph

# Rebuild graph object for tourism
g = convert_to_graph(graph_data, islands)

print( )

# === SKILL SHARING ===
print("=== Skill Sharing ===")
route = greedy_skill_sharing_route('Hawaii', graph_data, islands)
print("Leader’s Route for Skill Sharing:")
print(" → ".join(route))
print(f"Total Islands Visited: {len(route)}")

# === RESOURCE DISTRIBUTION ===
print("\n=== Resource Distribution ===")
dijkstra_tree(islands, graph_data, "Niihau")

# === TOURISM ROUTE ===
print("\n=== Tourism Route ===")

# No time limit
result = find_best_route(g, "Hawaii")
print("\n--- Tourist from Hawaii (No Time Limit) ---")
if result:
    print("Total Time:", result['total_time'])
    print("Path:", " → ".join(result['path']))
    print("Experiences Count:", result['experiences_count'])
    print("Unique Experiences:", ", ".join(result['unique_experiences']))
else:
    print("No good route found")

# 300-hour time limit
result = find_best_route(g, "Tahiti", max_time=300)
print("\n--- Tourist from Tahiti (Max 300 Hours) ---")
if result:
    print("Total Time:", result['total_time'])
    print("Path:", " → ".join(result['path']))
    print("Experiences Count:", result['experiences_count'])
    print("Unique Experiences:", ", ".join(result['unique_experiences']))
else:
    print("No good route found within the time limit")

# 100-hour time limit
result = find_best_route(g, "Rapanui", max_time=100)
print("\n--- Tourist from Rapanui (Max 100 Hours) ---")
if result:
    print("Total Time:", result['total_time'])
    print("Path:", " → ".join(result['path']))
    print("Experiences Count:", result['experiences_count'])
    print("Unique Experiences:", ", ".join(result['unique_experiences']))
else:
    print("No good route found within the time limit")
