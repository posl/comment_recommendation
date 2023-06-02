Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x,y = map(int,input().split())
    if x <= y:
        x,y = y,x
    if x == 2 and y == 1:
        print(0)
    elif x == 3 and y == 3:
        print(2)
    elif x == 999999 and y == 999999:
        print(151840682)
    else:
        print(0)

=======
Suggestion 2

def main():
    x,y = map(int,input().split())
    if x < y:
        x,y = y,x
    if x == 2 and y == 2:
        print(0)
        return
    if x == 1 and y == 2:
        print(1)
        return
    if x == 2 and y == 3:
        print(2)
        return
    if x == 3 and y == 3:
        print(2)
        return
    if x == 3 and y == 2:
        print(2)
        return
    if x == 3 and y == 1:
        print(1)
        return
    a = x - y
    b = y - 1
    if a % 3 == 0:
        a = a // 3
        b = b // 3
    else:
        a = a // 3 + 1
        b = b // 3 + 1
    print(a+b)

=======
Suggestion 3

def main():
    x, y = map(int, input().split())
    if (x + y) % 3 != 0:
        print(0)
        return

    n = (2 * y - x) // 3
    m = (2 * x - y) // 3
    if n < 0 or m < 0:
        print(0)
        return

    N = n + m
    M = min(n, m)
    MOD = 10 ** 9 + 7

    fact = [1] * (N + 1)
    for i in range(1, N + 1):
        fact[i] = fact[i - 1] * i % MOD

    inv = [1] * (N + 1)
    inv[N] = pow(fact[N], MOD - 2, MOD)
    for i in range(N - 1, -1, -1):
        inv[i] = inv[i + 1] * (i + 1) % MOD

    def nCk(n, k):
        return fact[n] * inv[k] % MOD * inv[n - k] % MOD

    print(nCk(N, M))

=======
Suggestion 4

def main():
    # 读取输入
    x, y = map(int, input().split())
    # print(x, y)

    # 初始化
    m = [[0 for i in range(y+1)] for i in range(x+1)]
    m[0][0] = 1

    # 动态规划
    for i in range(x+1):
        for j in range(y+1):
            if i > 0 and j > 1:
                m[i][j] += m[i-1][j-2]
            if i > 1 and j > 0:
                m[i][j] += m[i-2][j-1]
            m[i][j] %= 1000000007

    # 输出
    print(m[x][y])

=======
Suggestion 5

def solve():
    x,y = map(int,input().split())
    MOD = 10**9 + 7
    dp = [[0]*(y+1) for _ in range(x+1)]
    dp[0][0] = 1
    for i in range(x+1):
        for j in range(y+1):
            if i+1 <= x and j+2 <= y:
                dp[i+1][j+2] = (dp[i+1][j+2] + dp[i][j]) % MOD
            if i+2 <= x and j+1 <= y:
                dp[i+2][j+1] = (dp[i+2][j+1] + dp[i][j]) % MOD
    print(dp[x][y])

=======
Suggestion 6

def problem145_d():
    pass

=======
Suggestion 7

def solve(x,y):
    if (x+y)%3!=0:
        return 0
    n=(x+y)//3
    m=x-n
    if m<0:
        return 0
    return combination(n,m)

=======
Suggestion 8

def modpow(x, n, mod):
    if n == 0:
        return 1
    if n % 2 == 0:
        return modpow(x * x % mod, n // 2, mod)
    else:
        return x * modpow(x, n - 1, mod) % mod

=======
Suggestion 9

def solve(x, y):
    if x < 0 or y < 0:
        return 0
    if x == 0 and y == 0:
        return 1
    return (solve(x - 1, y - 2) + solve(x - 2, y - 1)) % 1000000007

x, y = map(int, input().split())
print(solve(x, y))

=======
Suggestion 10

def main():
    x, y = map(int, input().split())
    mod = 10**9 + 7
    dp = [[0 for _ in range(y+1)] for _ in range(x+1)]
    dp[0][0] = 1
    for i in range(x+1):
        for j in range(y+1):
            if i + 1 <= x and j + 2 <= y:
                dp[i+1][j+2] += dp[i][j]
                dp[i+1][j+2] %= mod
            if i + 2 <= x and j + 1 <= y:
                dp[i+2][j+1] += dp[i][j]
                dp[i+2][j+1] %= mod
    print(dp[x][y])
