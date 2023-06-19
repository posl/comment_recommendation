def get_input():
    N = int(input())
    XY = []
    for _ in range(N):
        x, y = map(int, input().split())
        XY.append((x, y))
    return N, XY
