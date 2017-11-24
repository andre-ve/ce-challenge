import pandas as pd

class Logger:

    def __init__(self, run_id):
        self._filename_iteration = 'exp_' + str(run_id) + '_iter.csv'
        self._filename_bot = 'exp_' + str(run_id) + '_bot.csv'
        self._filename_exp = 'exp_' + str(run_id) + '.csv'
        self._run_id = run_id
        self._iter_log = pd.DataFrame(columns = ['run_id', 'exp_id', 'iter', 'bots_count', 'bots_sum_age'])
        self._bot_arrival_log = pd.DataFrame(columns = ['run_id', 'exp_id', 'iter', 'type', 'age'])
        self._exp_log = pd.DataFrame(columns=['run_id', 'exp_id', 'grid_size', 'initial_bots', 'spawn_rate', 'o_penalty', 'bot_r'])
        
    def log_iteration(self, exp_id, iteration, exp):
        self._iter_log = self._iter_log.append({'run_id':self._run_id, 'exp_id': exp_id, 'iter':iteration, 'bots_count': exp.bot_count(), 'bots_sum_age':exp.bot_sum_age(iteration)}, ignore_index=True)
        
    def log_bot_arrival(self, exp_id, iteration, bot):
        self._bot_arrival_log = self._bot_arrival_log.append({'run_id':self._run_id, 'exp_id': exp_id, 'iter':iteration, 'type':bot.get_type(), 'age':bot.age(iteration)}, ignore_index=True)
        
    def log_experiment(self, exp_id, grid_size, initial_bots, spawn_rate, o_penalty, bot_r):
        self._exp_log = self._exp_log.append({'run_id':self._run_id, 'exp_id': exp_id, 'grid_size':grid_size, 'initial_bots':initial_bots, 'spawn_rate':spawn_rate, 'o_penalty':o_penalty, 'bot_r':bot_r}, ignore_index=True)
        
    def write_files(self):
        self._iter_log.to_csv(self._filename_iteration, index=False)
        self._bot_arrival_log.to_csv(self._filename_bot, index=False)
        self._exp_log.to_csv(self._filename_exp, index=False)