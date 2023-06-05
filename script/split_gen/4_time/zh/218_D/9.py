def get_input():
    n = int(raw_input())
    points = []
    for i in range(n):
        points.append(tuple(map(int, raw_input().split())))
    return points
