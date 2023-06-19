def solve():
    N, S, D = map(int, input().split())
    XY = [list(map(int, input().split())) for _ in range(N)]
    for X, Y in XY:
        if X < S and Y > D:
            print('Yes')
            return
    print('No')
