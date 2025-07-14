class Island:
    def __init__(self, name, population, experiences=None):
        self.name = name
        self.population = population
        self.last_visited = 0
        self.visited = False
        self.experiences = experiences if experiences else []

    def __repr__(self):
        return f"{self.name}(Pop: {self.population}, Last: {self.last_visited})"
