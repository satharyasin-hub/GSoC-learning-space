from mesa import Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation
from agent import SchellingAgent


class SchellingModel(Model):
    def __init__(self, width=20, height=20, density=0.8, homophily=0.5):

        super().__init__()  
        
        self.grid = MultiGrid(width, height, torus=True)
        self.schedule = RandomActivation(self)
        self.homophily = homophily

        agent_id = 0

        
        for cell_content, pos in self.grid.coord_iter():
            x, y = pos

            if self.random.random() < density:
                agent_type = self.random.choice([0, 1])

                agent = SchellingAgent(agent_id, self, agent_type)

                self.grid.place_agent(agent, (x, y))
                self.schedule.add(agent)

                agent_id += 1

    def step(self):
        self.schedule.step()