from ssp import Experiment

exp = Experiment(name='3', grid_size = 20, initial_bots = 10, spawn_rate = 2, iterations = 1000)

exp.run(grid_wait=True)