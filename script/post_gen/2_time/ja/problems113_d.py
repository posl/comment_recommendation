Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W, K = map(int, input().split())
    dp = [[0] * W for _ in range(H + 1)]
    dp[0][0] = 1
    for h in range(H):
        for w in range(W):
            if w == 0:
                dp[h + 1][w] = dp[h][w] + dp[h][w + 1]
            elif w == W - 1:
                dp[h + 1][w] = dp[h][w - 1] + dp[h][w]
            else:
                dp[h + 1][w] = dp[h][w - 1] + dp[h][w] + dp[h][w + 1]
    print(dp[H][K - 1] % (10 ** 9 + 7))

=======
Suggestion 2

def main():
    H, W, K = map(int, input().split())
    mod = 10 ** 9 + 7
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
            dp[h + 1][w] %= mod
    print(dp[H][K - 1])

main()

=======
Suggestion 3

def main():
    H, W, K = map(int, input().split())
    MOD = 10**9 + 7
    dp = [[0] * W for _ in range(H + 1)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if j == 0:
                dp[i + 1][j] = dp[i][j] + dp[i][j + 1]
            elif j == W - 1:
                dp[i + 1][j] = dp[i][j] + dp[i][j - 1]
            else:
                dp[i + 1][j] = dp[i][j - 1] + dp[i][j] + dp[i][j + 1]
            dp[i + 1][j] %= MOD
    print(dp[H][K - 1])

=======
Suggestion 4

def main():
    H, W, K = map(int, input().split())
    MOD = 10**9 + 7
    dp = [[0] * W for _ in range(H + 1)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if j == 0:
                dp[i + 1][j] = dp[i][j] + dp[i][j + 1]
            elif j == W - 1:
                dp[i + 1][j] = dp[i][j] + dp[i][j - 1]
            else:
                dp[i + 1][j] = dp[i][j] + dp[i][j - 1] + dp[i][j + 1]
            dp[i + 1][j] %= MOD
    print(dp[H][K - 1])

=======
Suggestion 5

def main():
    H, W, K = map(int, input().split())
    MOD = 10**9 + 7
    dp = [[0] * W for _ in range(H+1)]
    dp[0][0] = 1
    for h in range(H):
        for w in range(W):
            if w == 0:
                dp[h+1][w] += dp[h][w+1]
                dp[h+1][w] %= MOD
            elif w == W-1:
                dp[h+1][w] += dp[h][w-1]
                dp[h+1][w] %= MOD
            else:
                dp[h+1][w] += dp[h][w-1] + dp[h][w+1]
                dp[h+1][w] %= MOD
    print(dp[H][K-1])

=======
Suggestion 6

def main():
    H, W, K = map(int, input().split())
    MOD = 10**9 + 7
    dp = [[0] * W for _ in range(H+1)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if j == 0:
                dp[i+1][j] = dp[i][j+1]
            elif j == W-1:
                dp[i+1][j] = dp[i][j-1]
            else:
                dp[i+1][j] = dp[i][j-1] + dp[i][j+1]
    print(dp[H][K-1]%MOD)

=======
Suggestion 7

def main():
    H, W, K = map(int, input().split())
    MOD = 10**9 + 7

    dp = [[0] * W for _ in range(H+1)]
    dp[0][0] = 1

    for h in range(H):
        for w in range(W):
            if w == 0:
                dp[h+1][w] += dp[h][w+1]
                dp[h+1][w] += dp[h][w]
            elif w == W-1:
                dp[h+1][w] += dp[h][w-1]
                dp[h+1][w] += dp[h][w]
            else:
                dp[h+1][w] += dp[h][w-1]
                dp[h+1][w] += dp[h][w]
                dp[h+1][w] += dp[h][w+1]

    print(dp[H][K-1] % MOD)

=======
Suggestion 8

def memoize(f):
    cache = {}
    def _f(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return _f

@memoize

=======
Suggestion 9

def main():
    # H:高さ, W:幅, K:最終的にたどり着く縦棒の番号
    H, W, K = map(int, input().split())

    # dp[i][j]:i段目のj番目の縦棒の上端から下にたどり着くあみだくじの本数
    dp = [[0 for _ in range(W)] for _ in range(H + 1)]

    # i段目のj番目の縦棒の上端から下にたどり着くあみだくじの本数を計算する
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if j == 0:
                dp[i + 1][j] = dp[i][j] + dp[i][j + 1]
                dp[i + 1][j] %= 1000000007
            elif j == W - 1:
                dp[i + 1][j] = dp[i][j] + dp[i][j - 1]
                dp[i + 1][j] %= 1000000007
            else:
                dp[i + 1][j] = dp[i][j - 1] + dp[i][j] + dp[i][j + 1]
                dp[i + 1][j] %= 1000000007

    # 答えを出力する
    print(dp[H][K - 1])

=======
Suggestion 10

def main():
    H, W, K = map(int, input().split())
    MOD = 10**9 + 7

    # dp[i][j]: i段目のj本目の縦線にたどり着く場合の数
    dp = [[0] * W for _ in range(H+1)]
    dp[0][0] = 1

    # 横線を引く場所を全探索
    for i in range(H):
        for mask in range(1 << (W-1)):
            # 横線の連続をチェック
            if '11' in bin(mask):
                continue

            # 横線の左右の縦線を決定
            next = [j for j in range(W)]
            for j in range(W-2):
                if (mask >> j) & 1:
                    next[j+1] = next[j]
            for j in range(W-1, 0, -1):
                if (mask >> (j-1)) & 1:
                    next[j-1] = next[j]

            # dpテーブルを更新
            for j in range(W):
                dp[i+1][next[j]] += dp[i][j]
                dp[i+1][next[j]] %= MOD

    print(dp[H][K-1])
