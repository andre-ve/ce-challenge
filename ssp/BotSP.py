from .Bot import Bot

class BotSP(Bot):
    
    def __init__(self, grid, spawn_time, initial_position):
        Bot.__init__(self, grid, spawn_time, initial_position)
        self._type = 'SP'
        
    def ordered_positions(self):
        paths = []
        for neighbor in self._grid.neighbors(self._position):
            # takes too long time to compute to scale
            paths.append((neighbor, len(self._grid.shortest_path(source = neighbor, target = self._destination))))
        paths = sorted(paths, key=lambda path: path[1])
        return [neighbor[0] for neighbor in paths]