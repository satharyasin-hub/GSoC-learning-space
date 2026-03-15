from mesa import Agent


class SchellingAgent(Agent):
    def __init__(self, unique_id, model, agent_type):
        super().__init__(model)
        self.unique_id = unique_id
        self.type = agent_type

    def step(self):
        neighbors = self.model.grid.get_neighbors(
            self.pos, moore=True, include_center=False
        )

        similar = sum(1 for neighbor in neighbors if neighbor.type == self.type)

        if neighbors and similar / len(neighbors) < self.model.homophily:
            self.model.grid.move_to_empty(self)