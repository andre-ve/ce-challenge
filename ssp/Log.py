import pandas as pd

class Logger:

    def __init__(self, name = 'experiment_log'):
        self._filename_iteration = name + '_iter.csv'
        self._filename_bot = name + '_bot.csv'
        self._exp_name = name
        self._iter_log = pd.DataFrame(columns = ['name', 'iter', 'bots_count', 'bots_sum_age'])
        self._bot_arrival_log = pd.DataFrame(columns = ['name', 'iter', 'type', 'age'])
        
    def log_iteration(self, iteration, exp):
        self._iter_log = self._iter_log.append({'name': self._exp_name, 'iter':iteration, 'bots_count': exp.bot_count(), 'bots_sum_age':exp.bot_sum_age(iteration)}, ignore_index=True)
        
    def log_bot_arrival(self, iteration, bot):
        self._bot_arrival_log = self._bot_arrival_log.append({'name': self._exp_name, 'iter':iteration, 'type':bot.get_type(), 'age':bot.age(iteration)}, ignore_index=True)
        
    def write_files(self):
        self._iter_log.to_csv(self._filename_iteration, index=False)
        self._bot_arrival_log.to_csv(self._filename_bot, index=False)