import math
from operator import mul


class UnitObj:
    """
        Put the point in all possible places of unit. Will be check only half
    width and half length, because rectangle symmetric by x and y axis. Also,
    will be check division on 3 rooms by length and width.
    """
    MIN_ROOM_SIZE = 80
    MAX_ROOM_SIZE = 1000
    NUMBER_ROOMS = 3

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.unit_area = length * width
        self.possible_rooms = []
        self.combinations = [[1, 0, 1, 1], [0, 1, 1, 1]]

    def _area_vlidation(self, rooms):
        if not rooms: return False
        for room in rooms:
            if not self.MIN_ROOM_SIZE <= mul(*room) <= self.MAX_ROOM_SIZE:
                return False
        return True

    def _divide(self, x0, y0, r1, r2, r3, r4):
        x, y = self.length - x0, self.width - y0
        if r1 + r3 + r4 == 3:
            return (x0, y0), (x, y0), (self.length, y)
        if r2 + r3 + r4 == 3:
            return (x0, y0), (x0, y), (x, self.width)

    def _divide_hv(self, p0, length, width, inverted=False):
        if not self._area_vlidation([(p0, width)]):
            return
        for p1 in range(1, math.ceil((length - p0) / 2) + 1):
            if not self._area_vlidation([(p1, width)]):
                continue
            p2 = length - p0 - p1
            if not self._area_vlidation([(p2, width)]):
                continue
            if inverted:

                self.possible_rooms.append(
                    ((width, p0), (width, p1), (width, p2)))
            else:
                self.possible_rooms.append(
                    ((p0, width), (p1, width), (p2, width)))

    def calculate_possible_rooms(self):
        # Check the capacity of unit
        if not self.NUMBER_ROOMS * self.MIN_ROOM_SIZE <= self.unit_area <= \
                        self.NUMBER_ROOMS * self.MAX_ROOM_SIZE:
            return
        vertical= True
        if self.length == self.width:
            vertical = False
        for x in range(1, math.ceil(self.length / 2) + 1):
            self._divide_hv(x, self.length, self.width, inverted=False)
            for y in range(1, math.ceil(self.width / 2) + 1):
                for comb in self.combinations:
                    rooms_sizes = self._divide(x, y, *comb)
                    if self._area_vlidation(rooms_sizes):
                        self.possible_rooms.append(rooms_sizes)
                if vertical:
                    self._divide_hv(y, self.width, self.length, inverted=True)
            vertical = False

# Uncomment code below and run "$ python utils.py" for
# obtain possible rooms sizes. Setup length and width variables
if __name__ == '__main__':
    length1, width1 = 1000, 1
    u=UnitObj(length1, width1)
    u.calculate_possible_rooms()
    for struct in u.possible_rooms:
        print(struct)
    print('Number of variants:', len(u.possible_rooms))
