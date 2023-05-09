def get_input():
    N = int(input())
    points = []
    for i in range(N):
        points.append(list(map(int, input().split())))
    return N, points
