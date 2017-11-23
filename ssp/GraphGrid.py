import networkx as nx
from random import randint

class GraphGrid:

    def __init__(self, n = 10):
        self._n = n
        self._gg = nx.generators.lattice.grid_2d_graph(n, n)
        nx.set_node_attributes(self._gg, True, 'free')
    
    def initial_position(self, bot):
        pos_y = randint(0, self._n - 1)
        while not(self._gg.nodes[(pos_y, 0)]['free']):
            pos_y = randint(0, self._n - 1)
        return (pos_y, 0)

    def new_position(self, bot):
        ordered_positions = bot.ordered_positions()
        # print(ordered_positions)
        for position in ordered_positions:
            if self._gg.nodes[position]['free']:
                bot.set_position(position)
                #self._gg[position]['free'] ) = False
                break
                
    def set_position_free(self, position):
        self._gg.nodes[position]['free'] = True
        
    def set_position_busy(self, position):
        self._gg.nodes[position]['free'] = False
        
    def draw_grid(self):
        last_i = 0
        for node in self._gg.nodes:
            i, j = node
            if last_i != i:
                last_i = i
                print('')
            print(int(self._gg.nodes[node]['free']), end='')
            
    def get_random_destination(self):
        return (randint(0, self._n - 1), self._n - 1)
        
    def neighbors(self, position):
        return self._gg.neighbors(position)
        
    def shortest_path(self, source, target):
        return nx.shortest_path(self._gg, source = source, target = target)
        