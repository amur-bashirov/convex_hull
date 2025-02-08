# Uncomment this line to import some functions that can help
# you debug your algorithm
# from plotting import draw_line, draw_hull, circle_point
from plotting import plot_points


def compute_hull(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """Return the subset of provided points that define the convex hull"""
    points.sort(key=lambda p: (p[0], p[1]))
    print(points)
    DC(points)



    return points


def small_hulls(points):
    pass


def merge_hulls(left_hull, right_hull):
    pass


def DC(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    if len(points) > 3:
        median = len(points) // 2
        left =points[:median]
        right = points[median:]
        left_hull = DC(left)
        right_hull = DC(right)
    else:
        small_hulls(points)
    return merge_hulls(left_hull,right_hull)



if __name__ == '__main__':
    # To debug or run in your IDE
    # you can uncomment the lines below and modify the arguments as needed
    # import sys
    # sys.argv = ['main.py', '-n', '10', '--seed', '312', '--debug']

    compute_hull([(1, 2), (3, 5), (4, 1), (6, 7), (8, 3), (2, 6), (5, 4), (7, 2), (9, 5), (10, 1) , (12,3),(14,5)])