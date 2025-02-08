# Uncomment this line to import some functions that can help
# you debug your algorithm
# from plotting import draw_line, draw_hull, circle_point
from contextlib import nullcontext

from numpy.ma.core import right_shift

from plotting import plot_points, draw_hull, circle_point, draw_line


def compute_hull(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """Return the subset of provided points that define the convex hull"""
    points.sort(key=lambda p: (p[0], p[1]))
    print(points)
    DC(points)
    return points

def DC(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    if len(points) > 3:
        median = len(points) // 2
        left =points[:median]
        right = points[median:]
        left_hull = DC(left)
        right_hull = DC(right)
    else:
        draw_hull(points)
        return points
    return merge_hulls(left_hull,right_hull)

def slope(A, B):
    if A[0] == B[0]:
        return float('inf')  # Vertical line case
    else:
        return (A[1] - B[1]) / (A[0] - B[0])



def find_upper_tangent(left_hull, right_hull):
    q = right_hull[0]
    p = left_hull[-1]
    temp = [p, q]
    done = False


    circle_point(p)
    circle_point(q)
    draw_line(p, q)

    while done == False:
        done = True


        if len(left_hull) > 1:
            p_prev = left_hull[left_hull.index(p) - 1]
        else:
            p_prev = None
        if len(right_hull) > 1:
            q_prev = right_hull[right_hull.index(q) + 1]
        else:
            q_prev = None



        while slope(p, q) < slope(p, q_prev):
            q = q_prev
            temp = [p, q]
            circle_point(p)
            draw_line(p, q)
            done = False



        while slope(p, q) > slope(p_prev, q):
            p = p_prev
            temp = [p, q]
            circle_point(q)
            draw_line(p, q)
            done = False

    return temp



def find_lower_tangent(left_hull, right_hull):
    q = right_hull[0]
    p = left_hull[-1]
    temp = [p, q]
    done = False

    circle_point(p)
    circle_point(q)
    draw_line(p, q)

    while done == False:
        done = True

        if len(left_hull) > 1:
            p_prev = left_hull[left_hull.index(p) - 1]
        else:
            p_prev = None
        if len(right_hull) > 1:
            q_prev = right_hull[right_hull.index(q) - 1]
        else:
            q_prev = None


        while slope(q,p) < slope( q_prev, p):
            q = q_prev
            temp = [p, q]
            circle_point(q)
            draw_line(p, q)
            done = False

        while slope(p, q) < slope(p, p_prev):
            p = p_prev
            temp = [p, q]
            circle_point(p)
            draw_line(p, q)
            done = False



    return temp


def merge_hulls(left_hull, right_hull):
    upper_tangent = find_upper_tangent(left_hull,right_hull)
    lower_tangent = find_lower_tangent(left_hull, right_hull)
    merged_hull = upper_tangent + lower_tangent
    return merged_hull


if __name__ == '__main__':
    # To debug or run in your IDE
    # you can uncomment the lines below and modify the arguments as needed
    # import sys
    # sys.argv = ['main.py', '-n', '10', '--seed', '312', '--debug']

    compute_hull([(1, 2), (3, 5), (4, 1), (6, 7), (8, 3), (2, 6), (5, 4), (7, 2), (9, 5), (10, 1) , (12,3),(14,5)])