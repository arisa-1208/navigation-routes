from island import Island

# Island objects used across all algorithms
from island import Island

islands = {
    'Hawaii': Island('Hawaii', 1000, [
        {"name": "Surfing", "time": 10},
        {"name": "Volcano Hike", "time": 15}
    ]),
    'Tahiti': Island('Tahiti', 800, [
        {"name": "Lagoon Tour", "time": 12},
        {"name": "Black Sand Beach", "time": 8}
    ]),
    'Niihau': Island('Niihau', 150, [
        {"name": "Shell Diving", "time": 5}
    ]),
    'Rapanui': Island('Rapanui', 400, [
        {"name": "Moai Visit", "time": 20}
    ]),
    'Aotearoa': Island('Aotearoa', 1200, [
        {"name": "Maori Cultural Show", "time": 18},
        {"name": "Glacier Trek", "time": 22}
    ])
}


# Directed weighted graph for all routing
graph = {
    'Hawaii': {'Tahiti': 10, 'Niihau': 8},
    'Tahiti': {'Rapanui': 12, 'Aotearoa': 15},
    'Niihau': {'Tahiti': 5},
    'Rapanui': {'Aotearoa': 7},
    'Aotearoa': {'Hawaii': 20}
}

# Optional for Justin’s implementation (if he keeps using adjacency matrix)
adj = [
    [0, 1, 1, 0, 0],        
    [0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

# Travel time matrix for adjacency matrix graph (same order as adj)
travel = [
    [0, 4, 6, 0, 0],
    [0, 0, 0, 0, 8],
    [0, 0, 0, 7, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0]
]
