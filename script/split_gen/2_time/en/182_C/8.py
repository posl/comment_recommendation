def main():
    N = int(input())
    k = len(str(N))
    N = list(map(int, list(str(N))))
    N = N[::-1]
    N = N + N
    dp = [[0 for _ in range(3)] for _ in range(2 * k + 1)]
    dp[0][0] = 0
    for i in range(1, 2 * k + 1):
        for j in range(3):
            if dp[i - 1][j] == 0:
                continue
            dp[i][(j + N[i - 1]) % 3] = 1
            dp[i][j] = 1
    if dp[2 * k][0] == 1:
        print(min(k - dp[2 * k][0], k))
    else:
        print(-1)
