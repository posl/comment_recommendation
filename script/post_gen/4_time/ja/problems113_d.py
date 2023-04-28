Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W, K = map(int, input().split())
    dp = [[0 for _ in range(W)] for _ in range(H+1)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            for k in range(2**(W-1)):
                ok = True
                for l in range(W-2):
                    if ((k >> l) & 1) and ((k >> (l+1)) & 1):
                        ok = False
                if not ok:
                    continue
                nj = j
                if ((k >> j) & 1):
                    nj += 1
                elif j > 0 and ((k >> (j-1)) & 1):
                    nj -= 1
                dp[i+1][nj] += dp[i][j]
                dp[i+1][nj] %= 1000000007
    print(dp[H][K-1])

=======
Suggestion 2

def solve(H, W, K):
    if W == 1:
        return 1
    dp = [[0] * W for _ in range(H + 1)]
    dp[0][0] = 1
    for i in range(1, H + 1):
        for j in range(W):
            if j == 0:
                dp[i][j] = dp[i - 1][j + 1]
            elif j == W - 1:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
    return dp[H][K - 1]

=======
Suggestion 3

def solve(H, W, K):
    if W == 1:
        return 1
    elif K == 1:
        return solve(H, W - 1, K) + solve(H, W - 1, K + 1)
    elif K == W:
        return solve(H, W - 1, K) + solve(H, W - 1, K - 1)
    else:
        return solve(H, W - 1, K - 1) + solve(H, W - 1, K) + solve(H, W - 1, K + 1)

=======
Suggestion 4

def main():
    h,w,k = map(int,input().split())
    if k == 1:
        print(2**(w-1) % 1000000007)
    elif k == w:
        print(2**(w-2) % 1000000007)
    else:
        dp = [[0]*w for _ in range(h+1)]
        dp[0][0] = 1
        for i in range(h):
            for j in range(w):
                if j == 0:
                    dp[i+1][j] = dp[i][j]*2 + dp[i][j+1]
                elif j == w-1:
                    dp[i+1][j] = dp[i][j]*2 + dp[i][j-1]
                else:
                    dp[i+1][j] = dp[i][j]*2 + dp[i][j+1] + dp[i][j-1]
        print(dp[h][k-1] % 1000000007)

=======
Suggestion 5

def solve():
    H, W, K = map(int, input().split())
    if W == 1:
        print(1)
        return
    mod = 10**9+7
    dp = [[0]*W for _ in range(H+1)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            for k in range(1<<(W-1)):
                ok = True
                for l in range(W-2):
                    if (k>>l)&1 and (k>>(l+1))&1:
                        ok = False
                if not ok:
                    continue
                if j >= 1 and (k>>(j-1))&1:
                    dp[i+1][j-1] += dp[i][j]
                    dp[i+1][j-1] %= mod
                elif j <= W-2 and (k>>j)&1:
                    dp[i+1][j+1] += dp[i][j]
                    dp[i+1][j+1] %= mod
                else:
                    dp[i+1][j] += dp[i][j]
                    dp[i+1][j] %= mod
    print(dp[H][K-1])
    return

=======
Suggestion 6

def dfs(h,w,k):
    if w == 1:
        return 1
    if k == 1:
        return dfs(h,w-1,k+1)
    elif k == h:
        return dfs(h,w-1,k-1)
    else:
        return dfs(h,w-1,k-1) + dfs(h,w-1,k+1)

h,w,k = map(int,input().split())
print(dfs(h,w,k) % 1000000007)

=======
Suggestion 7

def solve():
    H, W, K = map(int, input().split())
    #dp[i][j] := i段目にいて、j番目の縦線にいる場合の数
    dp = [[0 for j in range(W)] for i in range(H+1)]
    dp[0][0] = 1
    for i in range(1, H+1):
        for j in range(W):
            if j == 0:
                dp[i][j] = dp[i-1][j] + dp[i-1][j+1]
            elif j == W-1:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]
            dp[i][j] %= 1000000007
    print(dp[H][K-1])

=======
Suggestion 8

def main():
    H, W, K = map(int, input().split())
    MOD = 1000000007

    # dp[i][j] : i段目でj番目の縦線にいるあみだくじの本数
    dp = [[0] * (W + 1) for _ in range(H + 1)]
    dp[0][1] = 1
    for i in range(H):
        for j in range(1, W + 1):
            # 左に移動
            if j > 1:
                dp[i + 1][j - 1] += dp[i][j]
                dp[i + 1][j - 1] %= MOD

            # 右に移動
            if j < W:
                dp[i + 1][j + 1] += dp[i][j]
                dp[i + 1][j + 1] %= MOD

            # 移動しない
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= MOD

    print(dp[H][K])

=======
Suggestion 9

def solve():
    H,W,K = map(int, input().split())
    # dp[i][j] = i段目にいて、jにいる通り数
    dp = [[0] * (W+1) for _ in range(H+1)]
    dp[0][1] = 1
    for i in range(H):
        for j in range(1, W+1):
            dp[i+1][j] = dp[i][j-1] * dp[i][j] * dp[i][j+1]
            dp[i+1][j] %= 1000000007
    print(dp[H][K])

=======
Suggestion 10

def get_permutation(n, r, mod):
    if r > n:
        return 0
    return (fact[n] * fact_inv[n-r]) % mod
