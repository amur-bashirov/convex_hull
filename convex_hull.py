# Uncomment this line to import some functions that can help
# you debug your algorithm
# from plotting import draw_line, draw_hull, circle_point
import math
from contextlib import nullcontext

from numpy.ma.core import right_shift

from plotting import plot_points, draw_hull, circle_point, draw_line, show_plot


def compute_hull(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """Return the subset of provided points that define the convex hull"""
    points.sort(key=lambda p: (p[0], p[1]))
    # print(points)
    # print()
    return DC(points)


def sort_clockwise(points):
    if len(points) <= 2:
        return points
    new_list = []
    first = points[0]
    new_list.append(first)
    rest = points[1:]
    rest.sort(key=lambda p: math.atan2(p[1] - first[1], p[0] - first[0]), reverse=True)
    return [first] + rest


def DC(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    if len(points) > 3:
        median = len(points) // 2
        left =points[:median]
        right = points[median:]
        # print(f"Split points into {left} and {right}")
        left_hull = DC(left)
        right_hull = DC(right)
        merged = merge_hulls(left_hull, right_hull)
        # print(f"Merge the two hulls {merged}")
        return merged
    else:
        sorted = sort_clockwise(points)
        # print(f"Split the points to the size of 2 or 3 ad sorted them clockwise {sorted}")
        return sorted


def slope(A, B):
    if A[0] == B[0]:
        return float('inf')
    else:
        return (A[1] - B[1]) / (A[0] - B[0])

def clockwise_next(points, index):
    next_index = (index + 1) % len(points)  # Ensures wrap-around
    next_point = points[next_index]
    return next_point, next_index

def counterclockwise_next(points, index):
    next_index = (index - 1) % len(points)  # Ensures wrap-around
    next_point = points[next_index]
    return next_point, next_index


def find_upper_tangent(left_hull, right_hull):
    left_copy = left_hull
    left_copy.sort(key=lambda p: (p[0], p[1]))
    p_idx = len(left_hull) - 1
    q_idx = 0
    q = right_hull[q_idx]
    p = left_copy[p_idx]
    p_idx = left_copy.index(p)
    temp = [p, q]
    done = False
    # print("Trying to find an upper tangent")

    if p_idx == 0:
        p_idx = len(left_hull)
    p_next = left_hull[p_idx - 1]
    p_idx -= 1

    if q_idx == len(right_hull) - 1:
        q_idx = -1
    q_next = right_hull[q_idx + 1]
    q_idx += 1

    while done == False:
        done = True

        for _ in range(len(right_hull)):
            orig_sl = slope(p,q)
            new_sl = slope(p,q_next)
            # print(f"Comparing {orig_sl} and {new_sl}")
            if orig_sl < new_sl:
                q = q_next
                if q_idx == len(right_hull) - 1:
                    q_idx = -1
                q_next = right_hull[q_idx + 1]
                q_idx += 1
                # print(f"Found new value of q for upper tangent: {p} -> {q}")
                temp = [p, q]
                done = False
            else:
                break

        for _ in range(len(left_hull)):
            orig_sl = slope(p,q)
            new_sl = slope(p_next,q)
            # print(f"Comparing {orig_sl} and {new_sl}")
            if orig_sl > new_sl:
                p = p_next
                if p_idx == 0:
                    p_idx = len(left_hull)
                p_next = left_hull[p_idx - 1]
                p_idx -= 1
                # print(f"Found new value of p for upper tangent: {p} -> {q}")
                temp = [p, q]
                done = False
            else:
                break
    draw_hull(left_hull)
    draw_hull(right_hull)

    draw_line(p,q)
    show_plot(block=True)
    print(f"Final values for upper tangent: {p} -> {q}")
    return temp




def find_lower_tangent(left_hull, right_hull):
    left_copy = left_hull
    left_copy.sort(key=lambda p: (p[0], p[1]))
    p_idx = len(left_hull) - 1
    q_idx = 0
    q = right_hull[q_idx]
    p = left_copy[p_idx]
    p_idx = left_copy.index(p)
    temp = [p, q]
    done = False
    # print("Trying to find a lower tangent")


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
            # print(f"Comparing {orig_sl} and {new_sl}")
            if orig_sl > new_sl:
                q = q_next
                if q_idx == 0:
                    q_idx = len(right_hull)
                q_next = right_hull[q_idx - 1]
                q_idx -= 1
                # print(f"New value lower tangent for q: {p} -> {q}" )
                temp = [p, q]
                done = False
            else:
                break


        for _ in range(len(left_hull)):
            orig_sl = slope( p,q)
            new_sl = slope( p_next,q)
            # print(f"Comparing {orig_sl} and {new_sl}")
            if orig_sl < new_sl:
                p = p_next
                if p_idx == len(left_hull) - 1:
                    p_idx = -1
                p_next = left_hull[p_idx + 1]
                p_idx += 1
                # print(f"New value lower tangent for p: {p} -> {q}")
                temp = [p, q]
                done = False
            else:
                break

    draw_hull(left_hull)
    draw_hull(right_hull)
    draw_line(p,q)
    show_plot(block=True)
    print(f"Final values for lower tangent: {p} -> {q}")
    return temp


def merge_hulls(left_hull, right_hull):
    print(f"Merging: {left_hull} and {right_hull}")
    draw_hull(left_hull)
    draw_hull(right_hull)
    show_plot(block=True)


    upper_tangent = find_upper_tangent(left_hull,right_hull)
    lower_tangent = find_lower_tangent(left_hull, right_hull)



    merged_hull = []



    index = 0
    merged_hull.append(left_hull[0])
    for _ in range(len(left_hull)):
        if left_hull[index] == upper_tangent[0]:
            break
        next, index = clockwise_next(left_hull, index)
        if next == upper_tangent[0]:
            merged_hull.append(upper_tangent[0])
            break
        merged_hull.append(next)


    index = right_hull.index(upper_tangent[1])
    merged_hull.append(upper_tangent[1])
    for _ in range(len(right_hull)):
        if right_hull[0] == lower_tangent[1] and lower_tangent[1] == upper_tangent[1]:
            break
        next,index = clockwise_next(right_hull, index)
        if next == lower_tangent[1] and lower_tangent[1] == upper_tangent[1]:
            break
        if next == lower_tangent[1]:
            merged_hull.append(lower_tangent[1])
            break
        merged_hull.append(next)


    if lower_tangent[0] not in merged_hull:
        merged_hull.append(lower_tangent[0])
    index = left_hull.index(lower_tangent[0])
    for _ in range(len(left_hull)):
        next, index = clockwise_next(left_hull, index)
        if next in merged_hull:
            break
        merged_hull.append(next)




    draw_hull(merged_hull)
    show_plot(block=True)
    print(f"Merged hull: {merged_hull}" + "\n")

    return merged_hull


print("Hello Matthew")