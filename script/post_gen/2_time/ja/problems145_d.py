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
    print(comb(N, X - N))

=======
Suggestion 2

def main():
    X, Y = map(int, input().split())
    if X < Y:
        X, Y = Y, X
    if (X + Y) % 3 != 0:
        print(0)
    else:
        n = (X + Y) // 3
        k = X - n
        print(comb(n, k, 10 ** 9 + 7))

=======
Suggestion 3

def main():
    MOD = 10**9+7
    X, Y = map(int, input().split())
    if (X+Y)%3 != 0:
        print(0)
        return
    N = (X+Y)//3
    if X>N or Y>N:
        print(0)
        return
    def comb(n, r):
        if r<0 or r>n:
            return 0
        r = min(r, n-r)
        return fac[n]*facinv[r]*facinv[n-r]%MOD
    fac = [1, 1]
    facinv = [1, 1]
    inv = [0, 1]
    for i in range(2, N+1):
        fac.append(fac[-1]*i%MOD)
        inv.append((-inv[MOD%i]*(MOD//i))%MOD)
        facinv.append(facinv[-1]*inv[-1]%MOD)
    print(comb(N, X))

=======
Suggestion 4

def main():
    X, Y = map(int, input().split())
    mod = 10**9 + 7

    if (X + Y) % 3 != 0:
        print(0)
        return

    N = (X + Y) // 3
    X -= N
    Y -= N

    if X < 0 or Y < 0:
        print(0)
        return

    ans = 1
    for i in range(N):
        ans *= (N - i)
        ans %= mod
    for i in range(X):
        ans *= pow(i + 1, mod - 2, mod)
        ans %= mod
    for i in range(Y):
        ans *= pow(i + 1, mod - 2, mod)
        ans %= mod

    print(ans)

=======
Suggestion 5

def main():
    x, y = map(int, input().split())
    mod = 10**9+7
    if (x+y) % 3 != 0:
        print(0)
        return
    n = (x+y) // 3
    if x < n or y < n:
        print(0)
        return
    x -= n
    y -= n
    print(comb(n, x, mod))

=======
Suggestion 6

def main():
    X, Y = map(int, input().split())
    MOD = 10**9+7

    if (X+Y)%3 != 0:
        print(0)
        return

    N = (X+Y)//3
    if X>N or Y>N:
        print(0)
        return

    def cmb(n, r, mod):
        if n<r:
            return 0
        r = min(r, n-r)
        return g1[n] * g2[r] * g2[n-r] % mod

    N = 2*10**6
    g1 = [1, 1] # 元テーブル
    g2 = [1, 1] #逆元テーブル
    inverse = [0, 1] #逆元テーブル計算用テーブル

    for i in range( 2, N + 1 ):
        g1.append( ( g1[-1] * i ) % MOD )
        inverse.append( ( -inverse[MOD % i] * (MOD//i) ) % MOD )
        g2.append( (g2[-1] * inverse[-1]) % MOD )

    print(cmb(N, N-X, MOD))

=======
Suggestion 7

def main():
    # input
    X, Y = map(int, input().split())

    # compute
    MOD = 10**9+7
    dp = [[0]*(Y+1) for _ in range(X+1)]
    dp[0][0] = 1
    for i in range(X+1):
        for j in range(Y+1):
            if i == 0 and j == 0:
                continue
            if i-1 >= 0 and j-2 >= 0:
                dp[i][j] += dp[i-1][j-2]
            if i-2 >= 0 and j-1 >= 0:
                dp[i][j] += dp[i-2][j-1]
            dp[i][j] %= MOD

    # output
    print(dp[X][Y])

=======
Suggestion 8

def main():
    # 入力
    X, Y = map(int, input().split())

    # 処理
    if (X + Y) % 3 != 0:
        print(0)
        return

    N = (X + Y) // 3
    if X > N or Y > N:
        print(0)
        return

    # 二項係数の計算
    # 組み合わせの数を求める
    # 10^9+7 で割った余りを求める
    def comb(n, r):
        x = 1
        y = 1
        for i in range(n, n - r, -1):
            x *= i
            x %= 1000000007
        for i in range(1, r + 1):
            y *= i
            y %= 1000000007
        return (x * pow(y, 1000000005, 1000000007)) % 1000000007

    print(comb(N, X))

=======
Suggestion 9

def main():
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        print(0)
        return

    # 3で割った余りが0の時のみ、XとYの差が3の倍数であれば、
    # (0,0)から(X,Y)までの移動方法が存在する
    if (X - Y) % 3 != 0:
        print(0)
        return

    # (X,Y)までの移動方法は、
    # (X+Y)/3回の右下の移動と、
    # (X-Y)/3回の右上の移動の組み合わせである
    # これは組み合わせの計算になる
    # ただし、(X+Y)/3のうち、(X-Y)/3回は右上の移動になるため、
    # (X+Y)/3から(X-Y)/3を引く
    # これは、(X+Y)/3C(X-Y)/3と同じ
    # これを高速に計算するために、
    # (X+Y)/3!/(X-Y)/3!の形で計算する
    # これは、(X+Y)!/(X-Y)!/(X+Y-2(X-Y))!の形で計算できる
    # これは、(X+Y)!(X-Y)!/(X+Y-2(X-Y))!の形で計算できる
    # これは、(X+Y)!(X-Y)!/(X-2Y)!の形で計算できる
    # これは、(X+Y)!(X-Y)!/(X-2Y)!の形で計算できる
    # これは、(X+Y)!(X-Y)!(X-2Y)!の形で計算できる
    # これは、(X+Y)!/(X-Y)!(X-2Y)!の形で計算できる
    # これは、(X+Y)!

=======
Suggestion 10

def make_mod_combination(n, mod):
    # mod で割った余りの階乗のリストを返す
    # n: 階乗の上限
    # mod: 余り
    fac = [1]
    for i in range(1, n+1):
        fac.append(fac[-1] * i % mod)
    return fac
