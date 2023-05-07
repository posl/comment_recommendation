def solve():
    N = int(input())
    XY = []
    P = []
    for _ in range(N):
        x, y, p = map(int, input().split())
        XY.append((x, y))
        P.append(p)
    ans = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            ans = max(ans, (abs(XY[i][0] - XY[j][0]) + abs(XY[i][1] - XY[j][1])) // P[i])
    print(ans + 1)
