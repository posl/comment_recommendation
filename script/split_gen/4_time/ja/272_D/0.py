def solve():
    N,M = map(int,input().split())
    ans = [[-1 for _ in range(N)] for _ in range(N)]
    ans[0][0] = 0
    for i in range(N):
        for j in range(N):
            if ans[i][j] == -1:
                continue
            for k in range(N):
                for l in range(N):
                    if ans[k][l] == -1 and (i-k)**2 + (j-l)**2 <= M:
                        ans[k][l] = ans[i][j] + 1
    for i in range(N):
        print(*ans[i])
