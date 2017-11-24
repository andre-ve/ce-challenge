from . import *
import time
import os

class Experiment:
    
    def __init__(self, exp_id, logger, grid_size = 10, initial_bots = 10, spawn_rate = 1, iterations = 1000, o_penalty = 0, bot_r = 1):
        self._grid = GraphGrid(grid_size)
        self._spawn_rate = spawn_rate
        self._iterations = iterations
        self._bot_r = bot_r
        self._o_penalty = o_penalty
        self._bots = []
        self._exp_id = exp_id
        for i in range(initial_bots):
            initial_position = self._grid.initial_position()
            if initial_position == (-1, 0): break
            b = BotN(self._grid, 0, initial_position, self._o_penalty, self._bot_r)
            b.set_random_destination()
            self._bots.append(b)
        self._log = logger
        self._log.log_experiment(exp_id = self._exp_id, grid_size = grid_size, initial_bots = initial_bots, spawn_rate = self._spawn_rate, o_penalty = self._o_penalty, bot_r = self._bot_r)
        
    def run(self, grid_wait=False):
        for i in range(self._iterations):
            iter_start_time = time.time()
            for bot in self._bots:
                bot.move()
            move_time = time.time()
            remaining_bots = []
            for bot in self._bots:
                if bot.arrived():
                    self._log.log_bot_arrival(self._exp_id, i, bot)
                else:
                    remaining_bots.append(bot)
            self._bots = remaining_bots
            arrived_bots_time = time.time()
            for j in range(self._spawn_rate):
                initial_position = self._grid.initial_position()
                if initial_position == (-1, 0): break
                b = BotN(self._grid, i, initial_position, self._o_penalty, self._bot_r)
                b.set_random_destination()
                self._bots.append(b)
            spawn_time = time.time()
            self._log.log_iteration(self._exp_id, i, self)
            if grid_wait:
                print('')
                os.system('cls')
                self._grid.draw_grid()
                print('')
                input('Iteration %i. Enter to continue:' % i)
            else:
                print(i, move_time - iter_start_time, arrived_bots_time - move_time, spawn_time - arrived_bots_time)
        self._grid.draw_grid()
        self._log.write_files()
        
    def bot_count(self):
        return len(self._bots)
        
    def bot_sum_age(self, current_iteration):
        s = 0
        for bot in self._bots:
            s += bot.age(current_iteration)
        return s