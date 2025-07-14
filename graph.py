def find_index(islands, name):
    for i, island in enumerate(islands):
        if island.name == name:
            return i
    return -1
