Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W, A, B = map(int, input().split())
    MOD = 10 ** 9 + 7
    dp = [[0] * (W + 1) for _ in range(H + 1)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            dp[i + 1][j + 1] += dp[i][j]
            dp[i + 1][j + 1] %= MOD
            if i + 1 < H and j + 1 < W and i + 1 - A >= 0 and j + 1 - B >= 0:
                dp[i + 1][j + 1] += dp[i + 1 - A][j + 1 - B]
                dp[i + 1][j + 1] %= MOD
    print(dp[H][W])

=======
Suggestion 2

def main():
    h, w, a, b = map(int, input().split())
    ans = 0
    for i in range(1 << h):
        for j in range(1 << w):
            cnt = 0
            for k in range(h):
                for l in range(w):
                    if (i >> k) & 1 and (j >> l) & 1:
                        cnt += 1
            if cnt == a * b:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    H, W, A, B = map(int, input().split())
    MOD = 10**9 + 7
    def comb(n, r):
        x = 1
        y = 1
        for i in range(r):
            x = x * (n - i) % MOD
            y = y * (i + 1) % MOD
        return x * pow(y, MOD - 2, MOD) % MOD
    ans = 0
    for i in range(H - B):
        ans += comb(A + i, i) * comb(W - A + H - B - i - 1, H - B - i - 1)
        ans %= MOD
    print(ans)

=======
Suggestion 4

def main():
    H, W, A, B = map(int, input().split())
    # H, W, A, B = 4, 4, 8, 0
    # H, W, A, B = 3, 3, 4, 1
    # H, W, A, B = 2, 2, 1, 2
    # H, W, A, B = 1, 1, 0, 1
    # H, W, A, B = 1, 1, 1, 0

    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    def combination(n, r):
        return factorial(n) // (factorial(n - r) * factorial(r))

    def count(H, W, A, B):
        if H == 1:
            return 1
        else:
            return combination(H + W - 2, H - 1) * count(H - 1, W - A, A, B)

    print(count(H, W, A, B))

=======
Suggestion 5

def main():
    H, W, A, B = map(int, input().split())
    print((H - B) * (W - A) * (H - B - 1) * (W - A - 1) // 4)

=======
Suggestion 6

def main():
    H, W, A, B = map(int, input().split())
    MOD = 10**9 + 7
    def cmb(n, r):
        if r < 0 or r > n:
            return 0
        r = min(r, n - r)
        return g1[n] * g2[r] * g2[n-r] % MOD
    N = H + W
    g1 = [1, 1] # 元テーブル
    g2 = [1, 1] #逆元テーブル
    inverse = [0, 1] #逆元テーブル計算用テーブル
    for i in range( 2, N + 1 ):
        g1.append( ( g1[-1] * i ) % MOD )
        inverse.append( ( -inverse[MOD % i] * (MOD//i) ) % MOD )
        g2.append( (g2[-1] * inverse[-1]) % MOD )
    ans = 0
    for i in range(B, W):
        ans += cmb(H-A-1+i, i) * cmb(A-1+W-i-1, A-1)
        ans %= MOD
    print(ans)

=======
Suggestion 7

def main():
    H, W, A, B = map(int, input().split())
    #print(H, W, A, B)
    #print(H * W, 2 * A + B)
    if H * W == 2 * A + B:
        print("OK")
    else:
        print("NG")

=======
Suggestion 8

def get_ways(h, w, a, b):
    # print(h, w, a, b)
    if h == 1 and w == 1:
        return 1
    if h == 1:
        return get_ways(h, w - 1, a, b - 1)
    if w == 1:
        return get_ways(h - 1, w, a - 1, b)
    if a == 0:
        return get_ways(h - 1, w, a, b - 1)
    if b == 0:
        return get_ways(h, w - 1, a - 1, b)
    return get_ways(h - 1, w, a, b - 1) + get_ways(h, w - 1, a - 1, b)

H, W, A, B = map(int, input().split())
print(get_ways(H, W, A, B))

I got TLE on this. I think I need to use memoization. I am not sure how to do that. Can you help?

Thanks

You can use a dictionary to memoize your function.

@harryharry

Thanks for your reply. I am not sure how to do that. Can you help?

Thanks

You can use a dictionary to memoize your function.

@harryharry

Thanks for your reply. I am not sure how to do that. Can you help?

Thanks

You can use a dictionary to memoize your function.

@harryharry

Thanks for your reply. I am not sure how to do that. Can you help?

Thanks

You can use a dictionary to memoize your function.

@harryharry

Thanks for your reply. I am not sure how to do that. Can you help?

Thanks

You can use a dictionary to memoize your function.

@harryharry

Thanks for your reply. I am not sure how to do that. Can you help?

Thanks

You can use a dictionary to memoize your function.

@harryharry

Thanks for your reply. I am not sure how to do that. Can you help?

Thanks

You can use a dictionary to memoize your function.

@harryharry

Thanks for your reply. I am not sure how to do that. Can you help?

Thanks

You can use

=======
Suggestion 9

def main():
    H, W, A, B = map(int, input().split())
    mod = 10**9+7
    # dp[i][j] = i行目までで、j個のAを使っている通り数
    dp = [[0 for _ in range(A+1)] for _ in range(H+1)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(A+1):
            dp[i+1][j] += dp[i][j]
            if j < A:
                dp[i+1][j+1] += dp[i][j]
    # 横にA個並べる通り数
    def comb(n, r):
        x = 1
        y = 1
        for i in range(r):
            x *= n-i
            y *= i+1
        return x // y
    # 縦にB個並べる通り数
    def comb2(n, r):
        x = 1
        y = 1
        for i in range(r):
            x *= n-i
            y *= i+1
        return x // y
    # 1行目にB個並べる通り数
    def comb3(n, r):
        x = 1
        y = 1
        for i in range(r):
            x *= n-i
            y *= i+1
        return x // y
    ans = 0
    # 1行目にB個並べた通り数を掛ける
    ans = comb3(W, B)
    # 2行目以降について
    for i in range(1, H):
        # 1行目のB個は使い切ったので、A個を使う通り数を掛ける
        ans *= dp[i][A]
        ans %= mod
        # 1行目のB個を使い切っていないので、1行目のB個を使わない通り数を掛ける
        ans *= comb(W-B, B)
        ans %= mod

=======
Suggestion 10

def solve(h, w, a, b):
    return 0
