from ssp import *
from itertools import product
import sys

# bots Neumann r = 1
exp_logger = Logger(sys.argv[1])
initial_bots_values = [10, 20, 50, 100]
spawn_rate_values = [1, 2, 3, 5, 8, 10, 15, 20]
o_penalty_values = list(range(10))
bot_r_values = list(range(10))

i = 0
for initial_bots_e, spawn_rate_e, o_penalty_e, bot_r_e in product(initial_bots_values, spawn_rate_values, o_penalty_values, bot_r_values):
    exp = Experiment(exp_id=i, logger=exp_logger, grid_size = 100, initial_bots = initial_bots_e, spawn_rate = spawn_rate_e, iterations = 10000, o_penalty = o_penalty_e, bot_r = bot_r_e)
    i += 1
    exp.run()