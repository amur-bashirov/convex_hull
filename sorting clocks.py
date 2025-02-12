import math

from convex_hull import slope


def sort(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    new_list = []
    first = points[0]
    new_list.append(first)
    rest = points[1:]
    rest.sort(key=lambda p: math.atan2(p[1] - first[1], p[0] - first[0]), reverse=True)
    return [first] + rest


def clockwise_next(points, index):
    next_index = (index + 1) % len(points)  # Ensures wrap-around
    next_point = points[next_index]
    return next_point, next_index

def counterclockwise_next(points, index):
    next_index = (index - 1) % len(points)  # Ensures wrap-around
    next_point = points[next_index]
    return next_point, next_index


def find_lower_tangent(left_hull, right_hull):
    p_idx = len(left_hull) - 1
    q_idx = 0
    q = right_hull[q_idx]
    p = left_hull[p_idx]
    temp = [p, q]
    done = False
    print("Trying to find a lower tangent")


    if p_idx == len(left_hull) - 1:
        p_idx = -1
    p_next = left_hull[p_idx + 1]
    p_idx += 1

    if q_idx == 0:
        q_idx = len(right_hull)
    q_next = right_hull[q_idx -1 ]
    q_idx -= 1

    while done == False:
        done = True




        while slope(p,q) < slope( p,q_next):
            q = q_next
            if q_idx == 0:
                q_idx = len(right_hull)
            q_next = right_hull[q_idx - 1]
            q_idx -= 1
            print(f"New value lower tangent for q: {p} -> {q}" )
            temp = [p, q]
           # circle_point(q)
           # draw_line(p, q)
            done = False



        while slope( p,q) < slope( p_next,q):
            p = p_next
            if p_idx == len(left_hull) - 1:
                p_idx = -1
            p_next = left_hull[p_idx + 1]
            p_idx += 1
            print(f"New value lower tangent for p: {p} -> {q}")
            temp = [p, q]
            done = False


    print(f"Final values for lower tangent: {p} -> {q}" "\n")
    return temp#@   2




def find_upper_tangent(left_hull, right_hull):
    p_idx = len(left_hull) - 1
    q_idx = 0
    q = right_hull[q_idx]
    p = left_hull[p_idx]
    temp = [p, q]
    done = False
    print("Trying to find an upper tangent")


    if p_idx == 0:
        p_idx = len(left_hull)
    p_next = left_hull[p_idx - 1]
    p_idx -= 1

    if q_idx == len(right_hull) - 1:
        q_idx = 0
    q_next = right_hull[q_idx + 1]
    q_idx += 1

    while done == False:
        done = True





        while slope(p, q) < slope(p, q_next):
            q = q_next
            if q_idx == len(right_hull) - 1:
                q_idx = -1
            q_next = right_hull[q_idx + 1]
            q_idx += 1
            print(f"Found new value of q for upper tangent: {p} -> {q}" )
            temp = [p, q]
            done = False



        while slope( p,q) > slope(  p_next,q):
            p = p_next
            if p_idx == 0:
                p_idx = len(left_hull)
            p_next = left_hull[p_idx - 1]
            p_idx -= 1
            print(f"Found new value of p for upper tangent: {p} -> {q}" )
            temp = [p, q]
            done = False


    print(f"Final values for upper tangent: {p} -> {q}" "\n")
    return temp


def find_upper_tangent2(left_hull, right_hull):
    p_idx = len(left_hull) - 1
    q_idx = 0
    q = right_hull[q_idx]
    p = left_hull[p_idx]
    temp = [p, q]
    done = False
    print("Trying to find an upper tangent")

    if p_idx == 0:
        p_idx = len(left_hull)
    p_next = left_hull[p_idx - 1]
    p_idx -= 1

    if q_idx == len(right_hull) - 1:
        q_idx = 0
    q_next = right_hull[q_idx + 1]
    q_idx += 1

    while done == False:
        done = True

        for _ in range(len(right_hull)):
            orig_sl = slope(p,q)
            new_sl = slope(p,q_next)
            print(f"Comparing {orig_sl} and {new_sl}")
            if orig_sl < new_sl:
                q = q_next
                if q_idx == len(right_hull) - 1:
                    q_idx = -1
                q_next = right_hull[q_idx + 1]
                q_idx += 1
                print(f"Found new value of q for upper tangent: {p} -> {q}")
                temp = [p, q]
                done = False
            else:
                if q_idx == len(right_hull) - 1:
                    q_idx = -1
                q_next = right_hull[q_idx + 1]
                q_idx += 1

        for _ in range(len(left_hull)):
            orig_sl = slope(p,q)
            new_sl = slope(p_next,q)
            print(f"Comparing {orig_sl} and {new_sl}")
            if orig_sl > new_sl:
                p = p_next
                if p_idx == 0:
                    p_idx = len(left_hull)
                p_next = left_hull[p_idx - 1]
                p_idx -= 1
                print(f"Found new value of p for upper tangent: {p} -> {q}")
                temp = [p, q]
                done = False
            else:
                if p_idx == 0:
                    p_idx = len(left_hull)
                p_next = left_hull[p_idx - 1]
                p_idx -= 1

    print(f"Final values for upper tangent: {p} -> {q}" "\n")
    return temp

def find_lower_tangent2(left_hull, right_hull):
    p_idx = len(left_hull) - 1
    q_idx = 0
    q = right_hull[q_idx]
    p = left_hull[p_idx]
    temp = [p, q]
    done = False
    print("Trying to find a lower tangent")


    if p_idx == len(left_hull) - 1:
        p_idx = -1
    p_next = left_hull[p_idx + 1]
    p_idx += 1

    if q_idx == 0:
        q_idx = len(right_hull)
    q_next = right_hull[q_idx -1 ]
    q_idx -= 1

    while done == False:
        done = True




        for _ in range(len(right_hull)):
            orig_sl = slope(p,q)
            new_sl = slope( p,q_next)
            print(f"Comparing {orig_sl} and {new_sl}")
            if orig_sl < new_sl:
                q = q_next
                if q_idx == 0:
                    q_idx = len(right_hull)
                q_next = right_hull[q_idx - 1]
                q_idx -= 1
                print(f"New value lower tangent for q: {p} -> {q}" )
                temp = [p, q]
                done = False
            else:
                if q_idx == 0:
                    q_idx = len(right_hull)
                q_next = right_hull[q_idx - 1]
                q_idx -= 1


        for _ in range(len(left_hull)):
            orig_sl = slope( p,q)
            new_sl = slope( p_next,q)
            print(f"Comparing {orig_sl} and {new_sl}")
            if orig_sl > new_sl:
                p = p_next
                if p_idx == len(left_hull) - 1:
                    p_idx = -1
                p_next = left_hull[p_idx + 1]
                p_idx += 1
                print(f"New value lower tangent for p: {p} -> {q}")
                temp = [p, q]
                done = False
            else:
                if p_idx == len(left_hull) - 1:
                    p_idx = -1
                p_next = left_hull[p_idx + 1]
                p_idx += 1



    print(f"Final values for lower tangent: {p} -> {q}" "\n")
    return temp



if __name__ == '__main__':
    points = [(2,4),(3, 2), (4, 3)]
    print(points)
    points.sort(key=lambda p: (p[0], p[1]))
    print()
    print(sort(points))
