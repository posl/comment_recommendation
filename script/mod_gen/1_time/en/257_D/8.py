def main():
    N = int(input())
    xy = [list(map(int, input().split())) for _ in range(N)]
    P = [int(input()) for _ in range(N)]
    for i in range(N):
        xy[i].append(P[i])
    xy.sort(key=lambda x: x[2])
    dp = [[float('inf')] * N for _ in range(N)]
    for i in range(N):
        dp[i][i] = 0
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j, N):
                if xy[j][2] * dp[i][j] >= abs(xy[i][0] - xy[k][0]) + abs(xy[i][1] - xy[k][1]):
                    dp[i][k] = min(dp[i][k], dp[i][j] + 1)
    print(min(dp[i][-1] for i in range(N)))

if __name__ == '__main__':
    main()