Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        print(0)
        return
    N = (X + Y) // 3
    if X < N or Y < N:
        print(0)
        return
    print(comb(2 * N, N, 10 ** 9 + 7))

=======
Suggestion 2

def main():
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        print(0)
        return
    N = (X + Y) // 3
    if X > N or Y > N:
        print(0)
        return
    print(comb(N, X))

=======
Suggestion 3

def main():
    x, y = map(int, input().split())
    if (x + y) % 3 != 0:
        print(0)
        return
    n = (x + y) // 3
    if x > n or y > n:
        print(0)
        return
    print(comb(n, x, 10 ** 9 + 7))

=======
Suggestion 4

def main():
    X, Y = map(int, input().split())

    if (X + Y) % 3 != 0:
        print(0)
        return

    N = (X + Y) // 3
    if X > N or Y > N:
        print(0)
        return

    mod = 10 ** 9 + 7
    fac = [1, 1]
    finv = [1, 1]
    inv = [0, 1]
    for i in range(2, N + 1):
        fac.append(fac[i - 1] * i % mod)
        inv.append(mod - inv[mod % i] * (mod // i) % mod)
        finv.append(finv[i - 1] * inv[i] % mod)

    def nCr(n, r):
        if n < r:
            return 0
        if n < 0 or r < 0:
            return 0
        return fac[n] * (finv[r] * finv[n - r] % mod) % mod

    print(nCr(N, X))

=======
Suggestion 5

def main():
    x, y = map(int, input().split())
    if (x+y)%3 != 0:
        print(0)
        return
    n = (x+y)//3
    if x < n or y < n:
        print(0)
        return
    mod = 10**9+7
    def comb(n, r):
        if r < 0 or r > n:
            return 0
        r = min(r, n-r)
        return fac[n] * finv[r] % mod * finv[n-r] % mod
    N = 2*n
    fac = [1, 1]
    finv = [1, 1]
    inv = [0, 1]
    for i in range(2, N+1):
        fac.append(fac[-1] * i % mod)
        inv.append(mod - inv[mod%i] * (mod//i) % mod)
        finv.append(finv[-1] * inv[-1] % mod)
    print(comb(N, n))

=======
Suggestion 6

def main():
    import sys
    input = sys.stdin.readline
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        print(0)
        return
    N = (X + Y) // 3
    if X > N or Y > N:
        print(0)
        return
    MOD = 10**9 + 7
    # X + Y = 3N
    # X = N + a, Y = N + b
    # a + b = N
    # a + b = N
    # a = N - b
    # X = N - b + b = N
    # Y = N - b + b = N
    # X + Y = 2N
    # N = (X + Y) // 3
    # X = Y = N - b
    # 2N - b = N
    # b = N
    # X = N - N = 0
    # Y = N - N = 0
    # X + Y = 0
    # N = (X + Y) // 3
    # X = Y = N - N = 0
    # 2N - 0 = N
    # 2N = N
    # N = 2
    # X = N - b + b = N
    # Y = N - b + b = N
    # X + Y = 2N
    # N = (X + Y) // 3
    # X = Y = N - b
    # 2N - b = N
    # b = N
    # X = N - N = 0
    # Y = N - N = 0
    # X + Y = 0
    # N = (X + Y) // 3
    # X = Y = N - N = 0
    # 2N - 0 = N
    # 2N = N
    # N = 1
    # X = N - b + b = N
    # Y = N - b + b = N
    # X + Y = 2N
    # N = (X + Y) // 3
    # X = Y

=======
Suggestion 7

def main():
    X, Y = map(int, input().split())
    X, Y = max(X, Y), min(X, Y)
    if (X + Y) % 3 != 0:
        print(0)
        return
    N = (X + Y) // 3
    M = X - N
    if M < 0:
        print(0)
        return
    MOD = 10**9 + 7
    ans = 1
    for i in range(N+1, N+M+1):
        ans = ans * i % MOD
    for i in range(1, M+1):
        ans = ans * pow(i, MOD-2, MOD) % MOD
    print(ans)

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    MOD = 10**9 + 7
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n + 1):
        for j in range(m + 1):
            if i + 1 <= n and j + 2 <= m:
                dp[i + 1][j + 2] += dp[i][j]
                dp[i + 1][j + 2] %= MOD
            if i + 2 <= n and j + 1 <= m:
                dp[i + 2][j + 1] += dp[i][j]
                dp[i + 2][j + 1] %= MOD
    print(dp[n][m])

=======
Suggestion 9

def main():
    # 入力
    X, Y = map(int, input().split())
    # 0,0に戻れるか判定
    if (X + Y) % 3 != 0:
        print(0)
        return
    # 0,0に戻れる場合
    # 0,0からの距離を求める
    dist = (X + Y) // 3
    # 0,0からの距離が遠い方の座標を求める
    if X > Y:
        x = dist
        y = dist - X
    else:
        x = dist - Y
        y = dist
    # nCrを求める
    n = x + y
    r = x
    # nCrの計算
    ans = 1
    for i in range(n, n - r, -1):
        ans *= i
    for i in range(1, r + 1):
        ans //= i
    # 余りを求める
    print(ans % (10 ** 9 + 7))

=======
Suggestion 10

def main():
    #入力
    X, Y = map(int, input().split())
    #初期化
    mod = 10**9+7
    #XとYの差が奇数の時は絶対到達できない
    if abs(X-Y)%2 == 1:
        print(0)
        return
    #XとYの差が偶数の時は到達可能
    #XとYの差の半分をNとすると、XとYはN回動かせる
    N = abs(X-Y)//2
    #XとYの差の半分を動かす方法はN通り
    #XとYの差の半分を動かす方法を決めると、XとYの差の半分を動かす方法は1通り
    #XとYの差の半分を動かす方法を決めると、XとYの差の半分を動かす方法は1通り
    #XとYの差の半分を動かす方法を決めると、XとYの差の半分を動かす方法は1通り
    #XとYの差の半分を動かす方法を決めると、XとYの差の半分を動かす方法は1通り
    #XとYの差の半分を動かす方法を決めると、XとYの差の半分を動かす方法は1通り
    #XとYの差の半分を動かす方法を決めると、XとYの差の半分を動かす方法は1通り
    #XとYの差の半分を動かす方法を決めると、XとYの差の半分を動かす方法は1通り
    #XとYの差の半分を動かす方法を決めると、XとYの差の
