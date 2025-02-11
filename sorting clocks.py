import math


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



if __name__ == '__main__':
    points = [(2,4),(3, 2), (4, 3)]
    print(points)
    points.sort(key=lambda p: (p[0], p[1]))
    print()
    print(sort(points))
