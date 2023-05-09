def main():
    N, M = map(int, input().split())
    INF = 10**18
    ans = [[INF]*N for _ in range(N)]
    ans[0][0] = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                for l in range(N):
                    if (i-k)**2+(j-l)**2 == M:
                        ans[i][j] = min(ans[i][j], ans[k][l]+1)
    for i in range(N):
        print(*ans[i])
