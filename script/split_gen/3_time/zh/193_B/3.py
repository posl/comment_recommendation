def solve():
    N = int(input())
    APX = [list(map(int, input().split())) for _ in range(N)]
    APX.sort(key=lambda x: x[0])
    print(APX)
    for i in range(N):
        if APX[i][2] > 0:
            print(APX[i][1])
            return
    print(-1)
