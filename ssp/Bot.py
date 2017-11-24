
class Bot:

    def __init__(self, grid, spawn_time, initial_position, o_penalty=0):
        self._grid = grid
        self._position = initial_position
        self._grid.set_position_busy(self._position)
        self._spawn_time = spawn_time
        self._type = '-'
        self._o_penalty = o_penalty
        
    def get_type(self):
        return self._type
        
    def set_position(self, position):
        self._grid.set_position_free(self._position)
        self._position = position
        self._grid.set_position_busy(self._position)
        
    def set_random_destination(self):
        self._destination = self._grid.get_random_destination()
        
    def ordered_positions(self):
        pass
        
    def distance_l1(self, position):
        d = 0
        for i in range(len(self._position)):
            d += abs(self._destination[i] - position[i]) + self._o_penalty*self._grid.is_position_busy(position)
        return d
        
    def move(self):
        self._grid.new_position(self)
        
    def arrived(self):
        if self._position == self._destination:
            # print(self._position)
            self._grid.set_position_free(self._position)
            return True
        return False
        
    def age(self, current_iteration):
        return current_iteration - self._spawn_time