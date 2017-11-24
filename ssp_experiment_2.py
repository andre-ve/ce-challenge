from ssp import *

# bots Neumann r = 1
exp = Experiment(name='2', grid_size = 100, initial_bots = 50, spawn_rate = 10, iterations = 10000)

exp.run()