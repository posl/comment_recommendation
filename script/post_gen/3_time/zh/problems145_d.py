Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x,y=map(int,input().split())
    if (x+y)%3!=0:
        print(0)
        return
    if x>y:
        x,y=y,x
    if x*2<y:
        print(0)
        return
    n=(x+y)//3
    x-=n
    y-=2*n
    ans=1
    m=10**9+7
    for i in range(1,n+1):
        ans=ans*(n-i+1)%m
        ans=ans*pow(i,m-2,m)%m
    print(ans)

=======
Suggestion 2

def problem145_d():
    pass

=======
Suggestion 3

def main():
    X, Y = map(int, input().split())
    MOD = 10**9 + 7
    dp = [[0 for _ in range(Y+1)] for _ in range(X+1)]
    dp[0][0] = 1
    for i in range(X+1):
        for j in range(Y+1):
            if i+1<=X and j+2<=Y:
                dp[i+1][j+2] += dp[i][j]
                dp[i+1][j+2] %= MOD
            if i+2<=X and j+1<=Y:
                dp[i+2][j+1] += dp[i][j]
                dp[i+2][j+1] %= MOD
    print(dp[X][Y])

=======
Suggestion 4

def main():
    # 读取输入
    X, Y = map(int, input().split())
    # 初始化
    MOD = 1000000007
    dp = [[0 for i in range(Y + 1)] for j in range(X + 1)]
    dp[0][0] = 1
    # 递推
    for i in range(X + 1):
        for j in range(Y + 1):
            if i + 1 <= X and j + 2 <= Y:
                dp[i + 1][j + 2] += dp[i][j]
            if i + 2 <= X and j + 1 <= Y:
                dp[i + 2][j + 1] += dp[i][j]
    # 打印
    print(dp[X][Y] % MOD)

=======
Suggestion 5

def solve(x, y):
    dp = [[0] * (y + 1) for i in range(x + 1)]
    dp[0][0] = 1
    for i in range(x + 1):
        for j in range(y + 1):
            if i + 1 <= x and j + 2 <= y:
                dp[i + 1][j + 2] = (dp[i + 1][j + 2] + dp[i][j]) % (10 ** 9 + 7)
            if i + 2 <= x and j + 1 <= y:
                dp[i + 2][j + 1] = (dp[i + 2][j + 1] + dp[i][j]) % (10 ** 9 + 7)
    return dp[x][y]

x, y = map(int, input().split())
print(solve(x, y))

=======
Suggestion 6

def main():
    x, y = map(int, input().split())
    if (x + y) % 3 != 0:
        print(0)
        return
    if 2 * x < y or 2 * y < x:
        print(0)
        return
    n = (2 * x - y) // 3
    m = (2 * y - x) // 3
    ans = 1
    mod = 10 ** 9 + 7
    for i in range(1, n + 1):
        ans = (ans * (m + i)) % mod
        ans = (ans * pow(i, mod - 2, mod)) % mod
    print(ans)

=======
Suggestion 7

def main():
    from sys import stdin
    from collections import deque
    from math import factorial
    from functools import reduce
    MOD = 10**9 + 7

    def comb(n, r):
        if n < r:
            return 0
        return factorial(n) * pow(factorial(r), MOD-2, MOD) * pow(factorial(n-r), MOD-2, MOD) % MOD

    def solve(x, y):
        if (x+y) % 3 != 0:
            return 0
        n = (x+y) // 3
        if x < n or y < n:
            return 0
        return comb(n, x-n)

    x, y = map(int, stdin.readline().split())
    print(solve(x, y))

=======
Suggestion 8

def main():
    x,y = map(int,input().split())
    mod = 10**9+7
    if (x+y)%3 != 0:
        print(0)
        return
    n = (x+y)//3
    m = x-n
    if m<0 or n<0:
        print(0)
        return
    if m>n:
        m,n = n,m
    if m==0:
        print(1)
        return
    ans = 1
    for i in range(1,m+1):
        ans = ans*(n-m+i)%mod
        ans = ans*pow(i,mod-2,mod)%mod
    print(ans)

=======
Suggestion 9

def solve(x, y):
    dp = [[0 for _ in range(y+1)] for _ in range(x+1)]
    dp[0][0] = 1
    for i in range(x+1):
        for j in range(y+1):
            if i >= 1 and j >= 2:
                dp[i][j] += dp[i-1][j-2]
            if i >= 2 and j >= 1:
                dp[i][j] += dp[i-2][j-1]
            dp[i][j] %= 1000000007
    return dp[x][y]

=======
Suggestion 10

def main():
    x,y = map(int,input().split())
    if (x+y)%3!=0:
        print(0)
        return
    n = (x+y)//3
    x = x-n
    y = y-n
    if x<0 or y<0:
        print(0)
        return
    if x>y:
        x,y = y,x
    ans = 1
    for i in range(x):
        ans = ans*(n-i)//(i+1)
    print(ans%1000000007)
