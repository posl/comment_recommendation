def get_input():
    N = int(input())
    points = []
    for i in range(N):
        points.append(tuple(map(int, input().split())))
    return points
