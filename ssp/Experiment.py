from . import *

class Experiment:
    
    def __init__(self, grid_size = 10, initial_bots = 10, spawn_rate = 1, iterations = 1000):
        self._grid = GraphGrid(grid_size)
        self._spawn_rate = spawn_rate
        self._iterations = iterations
        self._bots = []
        for i in range(initial_bots):
            b = Bot(self._grid)
            b.set_random_destination()
            self._bots.append(b)
        
    def run(self):
        for i in range(self._iterations):
            for bot in self._bots:
                bot.move()
            self._bots = [bot for bot in self._bots if not(bot.arrived())]
            for i in range(self._spawn_rate):
                b = Bot(self._grid)
                b.set_random_destination()
                self._bots.append(b)
        self._grid.draw_grid()