Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W, K = map(int, input().split())
    dp = [[0] * W for _ in range(H + 1)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if j == 0:
                dp[i + 1][j] = dp[i][j + 1]
                continue
            if j == W - 1:
                dp[i + 1][j] = dp[i][j - 1]
                continue
            dp[i + 1][j] = dp[i][j - 1] + dp[i][j + 1]
    print(dp[H][K - 1] % 1000000007)

=======
Suggestion 2

def main():
    H, W, K = map(int, input().split())
    dp = [[0] * (W + 2) for _ in range(H + 1)]
    dp[0][1] = 1
    for h in range(1, H + 1):
        for w in range(1, W + 1):
            for i in range(1 << (W - 1)):
                if i & (i << 1):
                    continue
                if i & (1 << (w - 1)):
                    dp[h][w - 1] += dp[h - 1][w]
                    dp[h][w - 1] %= 10**9 + 7
                elif (i >> (w - 1)) & 1:
                    dp[h][w + 1] += dp[h - 1][w]
                    dp[h][w + 1] %= 10**9 + 7
                else:
                    dp[h][w] += dp[h - 1][w]
                    dp[h][w] %= 10**9 + 7
    print(dp[H][K])

=======
Suggestion 3

def main():
    H, W, K = map(int, input().split())
    dp = [[0] * W for _ in range(H + 1)]
    dp[0][0] = 1
    for h in range(H):
        for w in range(W):
            if w == 0:
                dp[h + 1][w] = dp[h][w + 1]
            elif w == W - 1:
                dp[h + 1][w] = dp[h][w - 1]
            else:
                dp[h + 1][w] = dp[h][w - 1] + dp[h][w + 1]
    print(dp[H][K - 1] % (10 ** 9 + 7))

=======
Suggestion 4

def main():
    H, W, K = map(int, input().split())
    MOD = 10**9 + 7
    dp = [[0] * W for _ in range(H + 1)]
    dp[0][0] = 1
    for h in range(H):
        for i in range(2 ** (W - 1)):
            if '11' in bin(i):
                continue
            for j in range(W):
                if j > 0 and i >> (j - 1) & 1:
                    dp[h + 1][j - 1] += dp[h][j]
                    dp[h + 1][j - 1] %= MOD
                elif j < W - 1 and i >> j & 1:
                    dp[h + 1][j + 1] += dp[h][j]
                    dp[h + 1][j + 1] %= MOD
                else:
                    dp[h + 1][j] += dp[h][j]
                    dp[h + 1][j] %= MOD
    print(dp[H][K - 1])

=======
Suggestion 5

def main():
    H, W, K = map(int, input().split())
    MOD = 10**9 + 7
    dp = [[0] * W for _ in range(H + 1)]
    dp[0][0] = 1
    for h in range(H):
        for bit in range(1 << (W - 1)):
            if '11' in bin(bit):
                continue
            for w in range(W):
                if w > 0 and (bit >> (w - 1)) & 1:
                    dp[h + 1][w - 1] += dp[h][w]
                    dp[h + 1][w - 1] %= MOD
                elif w < W - 1 and (bit >> w) & 1:
                    dp[h + 1][w + 1] += dp[h][w]
                    dp[h + 1][w + 1] %= MOD
                else:
                    dp[h + 1][w] += dp[h][w]
                    dp[h + 1][w] %= MOD
    print(dp[H][K - 1])

=======
Suggestion 6

def main():
    h, w, k = map(int, input().split())
    mod = 10**9 + 7
    dp = [[0] * w for _ in range(h + 1)]
    dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            if j > 0:
                dp[i + 1][j - 1] += dp[i][j]
                dp[i + 1][j - 1] %= mod
            if j < w - 1:
                dp[i + 1][j + 1] += dp[i][j]
                dp[i + 1][j + 1] %= mod
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= mod
    print(dp[h][k - 1])

=======
Suggestion 7

def main():
    H, W, K = map(int, input().split())
    mod = 10**9+7
    dp = [[0] * W for _ in range(H+1)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if j == 0:
                dp[i+1][j] = dp[i][j] + dp[i][j+1]
            elif j == W-1:
                dp[i+1][j] = dp[i][j] + dp[i][j-1]
            else:
                dp[i+1][j] = dp[i][j] + dp[i][j-1] + dp[i][j+1]
            dp[i+1][j] %= mod
    print(dp[H][K-1])

=======
Suggestion 8

def solve(h, w, k):
    mod = 10**9 + 7
    dp = [[0] * (w + 1) for _ in range(h + 1)]
    dp[0][1] = 1
    for i in range(h):
        for j in range(1, w + 1):
            if j == 1:
                dp[i + 1][j] = dp[i][j] + dp[i][j + 1]
            elif j == w:
                dp[i + 1][j] = dp[i][j] + dp[i][j - 1]
            else:
                dp[i + 1][j] = dp[i][j - 1] + dp[i][j] + dp[i][j + 1]
    return dp[h][k] % mod

h, w, k = map(int, input().split())
print(solve(h, w, k))

=======
Suggestion 9

def main():
    h, w, k = map(int, input().split())
    dp = [0] * w
    dp[0] = 1
    for _ in range(h):
        new_dp = [0] * w
        for i in range(w):
            if i == 0:
                new_dp[i] += dp[i] + dp[i + 1]
            elif i == w - 1:
                new_dp[i] += dp[i] + dp[i - 1]
            else:
                new_dp[i] += dp[i] + dp[i - 1] + dp[i + 1]
        dp = new_dp
    print(dp[k - 1] % 10 ** 9 + 7)

=======
Suggestion 10

def amidakuji(H, W, K):
    # H is the height of the amidakuji
    # W is the width of the amidakuji
    # K is the index of the column we want to reach from the bottom.
    # The number of ways to reach the bottom of the Kth column from the top
    # is the number of ways to reach the bottom of the (K-1)th column from
    # the top, plus the number of ways to reach the bottom of the (K+1)th
    # column from the top.
    # The number of ways to reach the bottom of the Kth column from the top
    # is the number of ways to reach the bottom of the (K-1)th column from
    # the top, plus the number of ways to reach the bottom of the (K+1)th
    # column from the top.
    # The number of ways to reach the bottom of the Kth column from the top
    # is the number of ways to reach the bottom of the (K-1)th column from
    # the top, plus the number of ways to reach the bottom of the (K+1)th
    # column from the top.
    # The number of ways to reach the bottom of the Kth column from the top
    # is the number of ways to reach the bottom of the (K-1)th column from
    # the top, plus the number of ways to reach the bottom of the (K+1)th
    # column from the top.
    # The number of ways to reach the bottom of the Kth column from the top
    # is the number of ways to reach the bottom of the (K-1)th column from
    # the top, plus the number of ways to reach the bottom of the (K+1)th
    # column from the top.
    # The number of ways to reach the bottom of the Kth column from the top
    # is the number of ways to reach the bottom of the (K-1)th column from
    # the top, plus the number of ways to reach the bottom of the (K+1)th
    # column from the top.
    # The number of ways to reach the bottom of the Kth column from the top
    # is the number
