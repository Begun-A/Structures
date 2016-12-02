import operator
from functools import reduce
from unittest import skip

from django.test import SimpleTestCase

from apps.unit.utils import possible_room_sizes

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
                area=possible_room_sizes(l,w)
                if not len(area)==len(set(area)):
                    print(l,'x', w)
    @skip
    def test_on_commutative_lw(self):
        """ Test on commutative length and width variables """

        # Variables w and l  can change: 1<=w<=3000, 1<=l<=3000
        for l in range(1,3000):
            for w in range(3000, 1, -1):
                area1=set(possible_room_sizes(l,w))
                area2=set(possible_room_sizes(w,l))
                if not area1^area2:
                    print(l,'x',w)

    def test_check_area(self):
        """Test check equal sum of rooms areas and unit area"""

        # Variables width and length  can change:
        #  1<=width<=3000, 1<=length<=3000
        length, width = 3000, 1
        room_list = possible_room_sizes(length, width)
        for struct in room_list:
            areas_rooms = []
            for room in struct:
                areas_rooms.append(reduce(operator.mul,room))
            if length*width != sum(areas_rooms):
                print('Error in:', length, 'x', width)


