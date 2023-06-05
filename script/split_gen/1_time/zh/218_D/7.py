def get_point():
    N = int(input())
    points = []
    for i in range(N):
        points.append(tuple(map(int, input().split())))
    return N, points
