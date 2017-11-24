from .Bot import Bot

class BotN(Bot):
    
    def __init__(self, grid, spawn_time, initial_position, o_penalty = 0, r = 1):
        Bot.__init__(self, grid, spawn_time, initial_position, o_penalty)
        self._type = 'N'
        self._r = r
        self._o_penalty = o_penalty
        
    def ordered_positions(self):
        paths = []
        for neighbor in self._grid.neighbors(self._position):
            paths.append((neighbor, self.distance_l1(neighbor, self._r)))
        paths = sorted(paths, key=lambda path: path[1])
        return [neighbor[0] for neighbor in paths]
        
    def distance_l1(self, position, r):
        d = 0
        if r > 1:
            for neighbor in self._grid.neighbors(position):
                d += self.distance_l1(neighbor, r - 1)
        else:
            d += Bot.distance_l1(self, position)
        return d