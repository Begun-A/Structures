import operator
from functools import reduce
from unittest import skip

from django.test import SimpleTestCase

from apps.unit.utils import UnitObj

class PossibleRoomsTestCase(SimpleTestCase):
    """ Test for possible_room_sizes function
        !!!DANGER: Be careful unskip some tests, they doing a big load!!!
    """

    @skip
    def test_on_uniqueness(self):
        """ Test on uniqueness of possible rooms """

        # Variables w and l  can change: 1<=w<=3000, 1<=l<=3000
        for l in range(1,3000):
            for w in range(1, 3000):
                u=UnitObj(l,w)
                u.calculate_possible_rooms()
                if not len(u.possible_rooms)==len(set(u.possible_rooms)):
                    print(l,'x', w)
    @skip
    def test_on_commutative_lw(self):
        """ Test on commutative length and width variables """

        # Variables w and l  can change: 1<=w<=3000, 1<=l<=3000
        for l in range(1,3000):
            for w in range(3000, 1, -1):
                u1 = UnitObj(l, w)
                u1.calculate_possible_rooms()
                u2 = UnitObj(w,l)
                u2.calculate_possible_rooms()
                area1=set(u1.possible_rooms)
                area2=set(u2.possible_rooms)
                if not area1^area2:
                    print(l,'x',w)

    def test_check_area(self):
        """Test check equal sum of rooms areas and unit area"""

        # Variables width and length  can change:
        #  1<=width<=3000, 1<=length<=3000
        length, width = 3000, 1
        u = UnitObj(length, width)
        u.calculate_possible_rooms()
        for struct in u.possible_rooms:
            areas_rooms = []
            for room in struct:
                areas_rooms.append(reduce(operator.mul,room))
            if length*width != sum(areas_rooms):
                print('Error in:', length, 'x', width)


