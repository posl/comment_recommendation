Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H,W,K = map(int,input().

=======
Suggestion 2

def solve():
    H, W, K = map(int, input().split())
    dp = [[0 for _ in range(W)] for _ in range(H+1)]
    dp[0][0] = 1
    for h in range(H):
        for w in range(W):
            for k in range(1 << (W-1)):
                # 横線が引けない条件
                if ((k >> (W-2)) & 1) and ((k >> (W-3)) & 1):
                    continue
                # 横線が引けない条件
                if ((k >> (W-2)) & 1) and (w < W-2):
                    continue
                # 横線が引けない条件
                if ((k >> (W-3)) & 1) and (w > 0):
                    continue
                dp[h+1][w] += dp[h][w-1] if w > 0 else 0
                dp[h+1][w] += dp[h][w+1] if w < W-1 else 0
                dp[h+1][w] %= 1000000007
    print(dp[H][K-1])

=======
Suggestion 3

def main():
    H, W, K = map(int, input().split())
    print(H, W, K)

=======
Suggestion 4

def main():
    H, W, K = map(int, input().split())

    dp = [[0 for _ in range(W)] for _ in range(H+1)]
    dp[0][0] = 1

    for i in range(H):
        for j in range(W):
            for k in range(1 << (W - 1)):
                ok = True
                for l in range(W - 2):
                    if (k >> l) & 1 and (k >> (l + 1)) & 1:
                        ok = False
                        break
                if not ok:
                    continue
                if j >= 1 and (k >> (j - 1)) & 1:
                    dp[i + 1][j - 1] += dp[i][j]
                    dp[i + 1][j - 1] %= 1000000007
                elif j <= W - 2 and (k >> j) & 1:
                    dp[i + 1][j + 1] += dp[i][j]
                    dp[i + 1][j + 1] %= 1000000007
                else:
                    dp[i + 1][j] += dp[i][j]
                    dp[i + 1][j] %= 1000000007

    print(dp[H][K - 1])

=======
Suggestion 5

def solve():
    H, W, K = map(int, input().split())
    MOD = 10**9+7
    dp = [[0 for _ in range(W)] for _ in range(H+1)]
    dp[0][0] = 1
    for i in range(1, H+1):
        for j in range(W):
            if j == 0:
                dp[i][j] = dp[i-1][j] + dp[i-1][j+1]
            elif j == W-1:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]
            dp[i][j] %= MOD
    print(dp[H][K-1])

=======
Suggestion 6

def solve(h, w, k):
    if w == 1:
        return 1
    dp = [[0] * (w + 1) for _ in range(h + 1)]
    dp[0][1] = 1
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            dp[i][j] = dp[i - 1][j - 1] * dp[i - 1][j] + dp[i - 1][j] * dp[i - 1][j + 1]
    return dp[h][k] % 1000000007

h, w, k = map(int, input().split())
print(solve(h, w, k))

=======
Suggestion 7

def f(n, k):
    if k == 0 or k == n:
        return 1
    return f(n-1, k-1) + f(n-1, k)

h, w, k = map(int, input().split())
print(f(h, k-1) * f(h+1, w-k) % 1000000007)

=======
Suggestion 8

def main():
    H, W, K = map(int, input().split())
    #print(H, W, K)

    # dp[縦棒の数][横線の数]
    dp = [[0 for i in range(W+1)] for j in range(H+1)]

    # 初期値
    dp[0][0] = 1

    # dp[縦棒の数][横線の数] = dp[縦棒の数-1][横線の数-1] + dp[縦棒の数-1][横線の数] + dp[縦棒の数-1][横線の数+1]
    for i in range(1, H+1):
        for j in range(W+1):
            if j == 0:
                dp[i][j] = dp[i-1][j] + dp[i-1][j+1]
            elif j == W:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]

    #print(dp)
    print(dp[H][K-1] % 1000000007)

=======
Suggestion 9

def main():
    # 標準入力の取得
    H, W, K = map(int, input().split())

    # 処理
    # 答えを 1 000 000 007 で割った余りを出力すること.
    # 1 000 000 007 は素数なので、フェルマーの小定理より、
    # 1 000 000 007 で割った余りを求めるには、
    # 逆元を使って、a / b を a * b^-1 として計算することで求めることができる.
    # 逆元は、フェルマーの小定理より、
    # a * a^-1 ≡ 1 (mod p) となる a^-1 が存在する.
    # この a^-1 を a の逆元と呼び、a^-1 ≡ a^(p-2) (mod p) として求めることができる.
    # この a^-1 を求めるには、繰り返し二乗法を用いて、
    # a^(p-2) ≡ a^(p-2) mod p を求めれば良い.
    # 逆元を求めるには、拡張ユークリッドの互除法を用いて、
    # a * x + p * y = 1 を満たす x を求めれば良い.
    # 拡張ユークリッドの互除法を用いると、
    # a * x + p * y = 1 を満たす x と y を求めることができる.
    # この x が a の逆元となる.
    # 逆元の求め方は、以下のようになる.
    # 1. a * x + p * y = 1 を満たす x と y を求める.
    #

=======
Suggestion 10

def main():
    h,w,k = map(int,input().split())
    dp = [[[0]*w for _ in range(h+1)] for _ in range(w)]
    dp[0][0][0] = 1
    for i in range(h):
        for j in range(w):
            for k in range(2**(w-1)):
                for l in range(w-1):
                    if k & (1<<l):
                        if l-1>=0 and k & (1<<(l-1)):
                            dp[j][i+1][l-1] += dp[j][i][l]
                            dp[j][i+1][l-1] %= 1000000007
                        elif l+1<w-1 and k & (1<<(l+1)):
                            dp[j][i+1][l+1] += dp[j][i][l]
                            dp[j][i+1][l+1] %= 1000000007
                        else:
                            dp[j+1][i+1][l] += dp[j][i][l]
                            dp[j+1][i+1][l] %= 1000000007
                    else:
                        dp[j][i+1][l] += dp[j][i][l]
                        dp[j][i+1][l] %= 1000000007
    print(dp[k-1][h][0])
main()
