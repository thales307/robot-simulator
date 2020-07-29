EAST = (1, 0)
NORTH = (0, 1)
WEST = (-1, 0)
SOUTH = (0, -1)


class Robot:
    def __init__(self, direction=NORTH, x=0, y=0):
        self.coordinates = (x, y)
        self.direction = direction

    def move(self, change):
        for i in change:
            if i == 'R':
                self.direction = (self.direction[1], -self.direction[0])
            elif i == 'L':
                self.direction = (-self.direction[1], self.direction[0])
            else:
                self.coordinates = tuple(sum(x)for x in zip(
                    self.coordinates, self.direction))
