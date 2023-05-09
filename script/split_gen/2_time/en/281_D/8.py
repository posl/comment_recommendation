def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    # DP[i][j] = i番目までのAの中からj個選んだ時の総和の最大値
    DP = [[0 for i in range(K + 1)] for j in range(N + 1)]
    DP[0][0] = 1
    for i in range(1, N + 1):
        for j in range(1, K + 1):
            if DP[i - 1][j - 1] == 1:
                DP[i][j] = 1
                if A[i - 1] % D == 0:
                    DP[i][j] = DP[i - 1][j] | DP[i - 1][j - 1]
                else:
                    DP[i][j] = DP[i - 1][j]
    if DP[N][K] == 0:
        print(-1)
        return
    ans = 0
    for i in range(N, 0, -1):
        if DP[i][K] == 1 and DP[i - 1][K - 1] == 0:
            ans += A[i - 1]
            K -= 1
            if K == 0:
                break
    if ans % D == 0:
        print(ans)
    else:
        print(-1)
