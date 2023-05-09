def main():
    N, M = map(int, input().split())
    INF = 10**9
    # dp[i][j] := (1,1)から(i,j)までの最小操作回数
    dp = [[INF]*N for _ in range(N)]
    dp[0][0] = 0
    # (i,j)に移動できるマスの候補
    for i in range(N):
        for j in range(N):
            for di in [-1,0,1]:
                for dj in [-1,0,1]:
                    if di*dj!=0:
                        continue
                    if i+di<0 or j+dj<0 or i+di>=N or j+dj>=N:
                        continue
                    dp[i+di][j+dj] = min(dp[i+di][j+dj], dp[i][j]+1)
    # (i,j)から(i,j)に移動できるマスの候補
    for i in range(N):
        for j in range(N):
            for di in [-1,0,1]:
                for dj in [-1,0,1]:
                    if di*dj!=0:
                        continue
                    if i+di<0 or j+dj<0 or i+di>=N or j+dj>=N:
                        continue
                    dp[i+di][j+dj] = min(dp[i+di][j+dj], dp[i][j])
    for i in range(N):
        for j in range(N):
            if dp[i][j] > M:
                dp[i][j] = -1
            else:
                dp[i][j] = M - dp[i][j]
    for i in range(N):
        print(*dp[i])

if __name__ == '__main__':
    main()