def solve():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    S = input()
    x_min = 10**9
    x_max = 0
    y_min = 10**9
    y_max = 0
    for i in range(N):
        if S[i] == 'R':
            x_min = min(x_min, XY[i][0])
        elif S[i] == 'L':
            x_max = max(x_max, XY[i][0])
        elif S[i] == 'U':
            y_min = min(y_min, XY[i][1])
        elif S[i] == 'D':
            y_max = max(y_max, XY[i][1])
    if x_min > x_max or y_min > y_max:
        print('No')
    else:
        print('Yes')
