import math
def possible_room_sizes(length, width):
        min_size = 80
        max_size = 1000
        unit_rooms = 3
        unit_area = width * length

        # Check the capacity of unit
        if not unit_rooms*min_size <= unit_area <= unit_rooms*max_size:
            return []
        # Container for possible rooms
        rooms_list = []

        # Put the point in all possible places of unit.
        # I will be check only half width and half length,
        # because rectangle symmetric by x and y axis
        for x in range(1, math.ceil(length/2)+1):
            s1 = x*width
            if min_size<=s1<=max_size:
                for a1 in range(1, math.ceil((length - x)/2)+1):
                    s2 = a1*width
                    if min_size<=s2<=max_size:
                        a2 = length-x-a1
                        s3 = a2*width
                        if min_size<=s3<=max_size:
                            rooms_list.append(((x,width),
                                               (a1, width),
                                               (a2,width)))

            for y in range(1, math.ceil(width/2)+1):
                s1 = x*y
                if not min_size<=s1<=max_size:
                    continue

                # check x+ line
                a1, b1 = length - x, y
                s2 = a1*b1
                if min_size <= s2 <= max_size:
                    a2, b2 = length, width - y
                    s3 = a2*b2
                    if min_size <= s3 <= max_size:
                        rooms_list.append(((x,y), (a1,b1), (a2,b2)))

                # check y+ line
                a1, b1 = x, width - y
                s2 = a1*b1
                if min_size <= s2 <= max_size:
                    a2, b2 = length - x, width
                    s3 = a2*b2
                    if min_size <= s3 <= max_size:
                        rooms_list.append(((x,y), (a1,b1), (a2,b2)))
        for y in range(1, math.ceil(width/2)+1):
                s1 = y*length
                if min_size<=s1<=max_size:
                    for b1 in range(1, math.ceil((width - y)/2)+1):
                        s2 = b1*length
                        if min_size<=s2<=max_size:
                            b2 = width-y-b1
                            s3 = b2*length
                            if min_size<=s3<=max_size:
                                rooms_list.append(((length, y),
                                                   (length, b1),
                                                   (length, b2)))
        return  rooms_list

def test():
    for i in range(1,300):
        for j in range(1, 300):
            t=possible_room_sizes(i,j)
            if not len(t)==len(set(t)):
                print(i,j)


if __name__=='__main__':
    a=300
    b=5
    room_list = possible_room_sizes(a,b)
    for i in room_list:
        print(i)
        s = 0
        for m in range(len(i)):
            mult = 1
            for k in range(len(i[m])):
                mult *=i[m][k]
            s += mult
        if s!=a*b:
            break

    print(len(room_list))
    print(len(set(room_list)))

