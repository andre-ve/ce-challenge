
class Bot:

    def __init__(self, grid):
        self._grid = grid
        self._position = self._grid.initial_position(self)
        self._grid.set_position_busy(self._position)
        
    def set_position(self, position):
        self._grid.set_position_free(self._position)
        self._position = position
        self._grid.set_position_busy(self._position)
        
    def set_random_destination(self):
        self._destination = self._grid.get_random_destination()
        
    def ordered_positions(self):
        paths = []
        for neighbor in self._grid.neighbors(self._position):
            paths.append((neighbor, len(self._grid.shortest_path(source = neighbor, target = self._destination))))
        paths = sorted(paths, key=lambda path: path[1])
        return [neighbor[0] for neighbor in paths]
        
    def move(self):
        self._grid.new_position(self)
        
    def arrived(self):
        if self._position == self._destination:
            # print(self._position)
            self._grid.set_position_free(self._position)
            return True
        return False