def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    dp = [[0 for i in range(2**N)] for j in range(N)]
    for i in range(N):
        for j in range(2**N):
            for k in range(N):
                if j & (1 << k) == 0:
                    dp[i][j | (1 << k)] = max(dp[i][j | (1 << k)], dp[i][j] ^ A[i][k])
    ans = 0
    for i in range(2**N):
        ans = max(ans, dp[N-1][i])
    print(ans)
