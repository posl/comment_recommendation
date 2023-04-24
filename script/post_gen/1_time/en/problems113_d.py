Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h, w, k = map(int, input().split())
    dp = [[0] * w for _ in range(h + 1)]
    dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            if j == 0:
                dp[i + 1][j] = dp[i][j + 1] + dp[i][j]
            elif j == w - 1:
                dp[i + 1][j] = dp[i][j - 1] + dp[i][j]
            else:
                dp[i + 1][j] = dp[i][j - 1] + dp[i][j] + dp[i][j + 1]
    print(dp[h][k - 1] % (10 ** 9 + 7))

=======
Suggestion 2

def main():
    H, W, K = map(int, input().split())
    dp = [[0] * (W + 1) for _ in range(H + 1)]
    dp[0][1] = 1
    mod = 10 ** 9 + 7
    for i in range(H):
        for j in range(1, W + 1):
            if j == 1:
                dp[i + 1][j] = dp[i + 1][j] + dp[i][j] + dp[i][j + 1]
            elif j == W:
                dp[i + 1][j] = dp[i + 1][j] + dp[i][j] + dp[i][j - 1]
            else:
                dp[i + 1][j] = dp[i + 1][j] + dp[i][j] + dp[i][j - 1] + dp[i][j + 1]
            dp[i + 1][j] %= mod
    print(dp[H][K])

=======
Suggestion 3

def main():
    H, W, K = map(int, input().split())
    dp = [[0] * W for _ in range(H + 1)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if j > 0:
                dp[i + 1][j - 1] += dp[i][j]
            if j < W - 1:
                dp[i + 1][j + 1] += dp[i][j]
            dp[i + 1][j] += dp[i][j]
    print(dp[H][K - 1] % 1000000007)

=======
Suggestion 4

def solve(h, w, k):
    mod = 10 ** 9 + 7
    dp = [[0] * w for _ in range(h + 1)]
    dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            if j == 0:
                dp[i + 1][j] = dp[i][j] * (w - 1)
                dp[i + 1][j + 1] = dp[i][j]
            elif j == w - 1:
                dp[i + 1][j] = dp[i][j] * (w - 1)
                dp[i + 1][j - 1] = dp[i][j]
            else:
                dp[i + 1][j] = dp[i][j] * (w - 2)
                dp[i + 1][j - 1] = dp[i][j]
                dp[i + 1][j + 1] = dp[i][j]
    return dp[h][k - 1] % mod

=======
Suggestion 5

def main():
    H, W, K = map(int, input().split())
    dp = [[0] * (W + 1) for i in range(H + 1)]
    dp[0][1] = 1
    MOD = 10 ** 9 + 7
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            if j == 1:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j + 1]
            elif j == W:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] + dp[i - 1][j + 1]
            dp[i][j] %= MOD
    print(dp[H][K])

=======
Suggestion 6

def main():
    H, W, K = map(int, input().split())
    MOD = 1000000007

    dp = [[0] * W for _ in range(H+1)]
    dp[0][0] = 1
    for h in range(H):
        for i in range(2**(W-1)):
            if '11' in bin(i):
                continue
            for j in range(W):
                if j > 0 and i & (1 << (j-1)):
                    dp[h+1][j-1] += dp[h][j]
                    dp[h+1][j-1] %= MOD
                elif j < W-1 and i & (1 << j):
                    dp[h+1][j+1] += dp[h][j]
                    dp[h+1][j+1] %= MOD
                else:
                    dp[h+1][j] += dp[h][j]
                    dp[h+1][j] %= MOD

    print(dp[H][K-1])

=======
Suggestion 7

def main():
    H, W, K = map(int, input().split())
    mod = 10**9+7
    dp = [[0]*(W+2) for _ in range(H+1)]
    dp[0][1] = 1
    for i in range(H):
        for j in range(1, W+1):
            if (dp[i][j-1] and dp[i][j+1]) or (dp[i][j-1] and j==W) or (dp[i][j+1] and j==1):
                continue
            dp[i+1][j] = dp[i][j-1] + dp[i][j+1]
    print(dp[H][K]%mod)

=======
Suggestion 8

def main():
    H, W, K = map(int, input().split())
    MOD = 10 ** 9 + 7
    dp = [[0] * (W + 2) for i in range(H + 1)]
    dp[0][1] = 1
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            dp[i][j] = dp[i - 1][j]
            if j > 1:
                dp[i][j] += dp[i - 1][j - 1]
            if j < W:
                dp[i][j] += dp[i - 1][j + 1]
            dp[i][j] %= MOD
    print(dp[H][K])

=======
Suggestion 9

def solve(h, w, k):
    if w == 1:
        return 1
    MOD = 10 ** 9 + 7
    dp = [[0] * w for _ in range(h + 1)]
    dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            if j == 0:
                dp[i + 1][j] = dp[i][j + 1]
            elif j == w - 1:
                dp[i + 1][j] = dp[i][j - 1]
            else:
                dp[i + 1][j] = dp[i][j - 1] + dp[i][j + 1]
    return dp[h][k - 1] % MOD

=======
Suggestion 10

def solve(h, w, k):
    # dp[i][j]: i段目のjの位置にいるパターン数
    dp = [[0] * w for _ in range(h + 1)]
    dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            if j == 0:
                dp[i + 1][j] = dp[i][j] + dp[i][j + 1]
            elif j == w - 1:
                dp[i + 1][j] = dp[i][j] + dp[i][j - 1]
            else:
                dp[i + 1][j] = dp[i][j] + dp[i][j - 1] + dp[i][j + 1]
    return dp[h][k - 1] % 1000000007
