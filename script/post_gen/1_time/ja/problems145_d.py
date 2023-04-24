Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        print(0)
        return
    if X > 2 * Y or Y > 2 * X:
        print(0)
        return
    if X == 0 and Y == 0:
        print(1)
        return
    if X == 0 or Y == 0:
        print(1)
        return
    if X == Y:
        print(2)
        return
    print(0)

=======
Suggestion 2

def solve(x, y):
    if x == 0 or y == 0:
        return 0
    elif x == 1 and y == 1:
        return 2
    elif x == 1 or y == 1:
        return max(x, y)
    else:
        return (solve(x - 1, y) + solve(x, y - 1)) % 1000000007

x, y = map(int, input().split())
print(solve(x, y))

=======
Suggestion 3

def main():
    X, Y = map(int, input().split())
    mod = 10**9 + 7
    if (X+Y)%3 != 0:
        print(0)
        exit()
    n = (X+Y)//3
    m = min(X, Y)
    if n > m:
        print(0)
        exit()
    ans = 1
    for i in range(n):
        ans *= (m-i)
        ans %= mod
    for i in range(1, n+1):
        ans *= pow(i, mod-2, mod)
        ans %= mod
    print(ans)

=======
Suggestion 4

def main():
    X,Y = map(int, input().split())
    if (X+Y)%3 != 0:
        print(0)
        exit()
    n = (2*Y-X)//3
    m = (2*X-Y)//3
    if n < 0 or m < 0:
        print(0)
        exit()
    mod = 10**9+7
    fact = [1,1]
    for i in range(2,n+m+1):
        fact.append((fact[-1]*i)%mod)
    invfact = [1,1]
    for i in range(2,n+m+1):
        invfact.append((invfact[-1]*pow(i,mod-2,mod))%mod)
    print((fact[n+m]*invfact[n]*invfact[m])%mod)

=======
Suggestion 5

def main():
    x,y = map(int,input().split())
    if (x+y)%3 != 0:
        print(0)
        exit()
    n = (x+y)//3
    m = min(x,y)-n
    if m < 0:
        print(0)
        exit()
    mod = 10**9+7
    #print(n,m)
    ans = 1
    for i in range(n-m+1,n+1):
        ans *= i
        ans %= mod
    for i in range(1,m+1):
        ans *= pow(i,mod-2,mod)
        ans %= mod
    print(ans)

=======
Suggestion 6

def main():
    x, y = map(int, input().split())
    if (x+y)%3 != 0:
        print(0)
        exit()
    n = (x+y)//3
    m = (2*x-y)//3
    if n < 0 or m < 0:
        print(0)
        exit()
    print(combination(n, m, 10**9+7))

=======
Suggestion 7

def solve():
    x, y = map(int, input().split())

    if (x+y)%3 != 0:
        print(0)
        return

    n = (x+y)//3
    m = min(x, y) - n

    if m < 0:
        print(0)
        return

    ans = 1
    for i in range(n):
        ans *= (n-i)
        ans %= MOD
    for i in range(n):
        ans *= pow(i+1, MOD-2, MOD)
        ans %= MOD

    for i in range(m):
        ans *= (m-i)
        ans %= MOD
    for i in range(m):
        ans *= pow(i+1, MOD-2, MOD)
        ans %= MOD

    print(ans)

MOD = 10**9+7
solve()

=======
Suggestion 8

def main():
    x,y = map(int, input().split())
    if (x+y)%3 != 0:
        print(0)
        return
    else:
        n = (x+y)//3
    if x < n or y < n:
        print(0)
        return
    else:
        x -= n
        y -= n
    MOD = 10**9+7
    fac = [1, 1]
    finv = [1, 1]
    inv = [0, 1]
    for i in range(2, n+1):
        fac.append(fac[i-1] * i % MOD)
        inv.append(MOD - inv[MOD%i] * (MOD//i) % MOD)
        finv.append(finv[i-1] * inv[i] % MOD)
    def comb(n, r, MOD):
        if r < 0 or r > n:
            return 0
        else:
            return fac[n] * (finv[r] * finv[n-r] % MOD) % MOD
    print(comb(x+y, x, MOD))

=======
Suggestion 9

def main():
    X, Y = map(int, input().split())
    MOD = 10 ** 9 + 7

    # 1 <= X <= 10^6
    # 1 <= Y <= 10^6
    # 1 <= i <= X
    # 1 <= j <= Y
    # dp[i][j] = (i, j) にナイトの駒を移動させる方法の数
    dp = [[0] * (Y + 1) for _ in range(X + 1)]
    dp[0][0] = 1

    for i in range(X + 1):
        for j in range(Y + 1):
            if i + 1 <= X and j + 2 <= Y:
                dp[i + 1][j + 2] += dp[i][j]
                dp[i + 1][j + 2] %= MOD
            if i + 2 <= X and j + 1 <= Y:
                dp[i + 2][j + 1] += dp[i][j]
                dp[i + 2][j + 1] %= MOD

    print(dp[X][Y])

=======
Suggestion 10

def get_input():
    x, y = map(int, input().split())
    return x, y
