import math


def possible_room_sizes(length, width):
    """
        Put the point in all possible places of unit. Will be check only half
    width and half length, because rectangle symmetric by x and y axis. Also,
    will be check division on 3 rooms by length and width.


    :param length: int object; length of Unit
    :param width: int object; width of Unit
    :return: list object; list of possible rooms sizes
    """
    min_size = 80
    max_size = 1000
    unit_rooms = 3
    unit_area = width * length

    # Check the capacity of unit
    if not unit_rooms * min_size <= unit_area <= unit_rooms * max_size:
        return []
    # Container for possible rooms
    rooms_list = []

    # Step by length
    for x in range(1, math.ceil(length / 2) + 1):
        # Division on 3 rooms by length
        s1 = x * width
        if min_size <= s1 <= max_size:
            for a1 in range(1, math.ceil((length - x) / 2) + 1):
                s2 = a1 * width
                if min_size <= s2 <= max_size:
                    a2 = length - x - a1
                    s3 = a2 * width
                    if min_size <= s3 <= max_size:
                        rooms_list.append(((x, width),
                                           (a1, width),
                                           (a2, width)))
        # Put the point and rays sets: {R0=1, R1=1, R2=1, R3=0}
        #                              {R0=1, R1=1, R2=0, R3=1}
        for y in range(1, math.ceil(width / 2) + 1):

            s1 = x * y
            if not min_size <= s1 <= max_size:
                continue

            # check {R0=1, R1=1, R2=0, R3=1}
            a1, b1 = length - x, y
            s2 = a1 * b1
            if min_size <= s2 <= max_size:
                a2, b2 = length, width - y
                s3 = a2 * b2
                if min_size <= s3 <= max_size:
                    rooms_list.append(((x, y), (a1, b1), (a2, b2)))

            # check {R0=1, R1=1, R2=1, R3=0}
            a1, b1 = x, width - y
            s2 = a1 * b1
            if min_size <= s2 <= max_size:
                a2, b2 = length - x, width
                s3 = a2 * b2
                if min_size <= s3 <= max_size:
                    rooms_list.append(((x, y), (a1, b1), (a2, b2)))

    # Division on 3 rooms by width
    if length == width:
        return rooms_list
    for y in range(1, math.ceil(width / 2) + 1):
        s1 = y * length
        if min_size <= s1 <= max_size:
            for b1 in range(1, math.ceil((width - y) / 2) + 1):
                s2 = b1 * length
                if min_size <= s2 <= max_size:
                    b2 = width - y - b1
                    s3 = b2 * length
                    if min_size <= s3 <= max_size:
                        rooms_list.append(((length, y),
                                           (length, b1),
                                           (length, b2)))
    return rooms_list

# Uncomment code below and run "$ python utils.py" for
# obtain possible rooms sizes. Setup length and width variables
if __name__=='__main__':
    length, width = 200, 3
    room_list = possible_room_sizes(length,width)
    for struct in room_list:
        print(struct)
    print('Number of variants:', len(room_list))
