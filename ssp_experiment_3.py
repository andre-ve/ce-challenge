from ssp import Experiment

exp = Experiment(name='3', grid_size = 30, initial_bots = 10, spawn_rate = 10, iterations = 1000, o_penalty = 1, bot_r = 2)

exp.run(grid_wait=True)