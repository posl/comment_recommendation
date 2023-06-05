Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    mod = 998244353

    dp = [[0 for i in range(3001)] for j in range(n+1)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(a[i], b[i]+1):
            dp[i+1][j] = dp[i][j]
        for j in range(1, 3001):
            dp[i+1][j] += dp[i+1][j-1]
            dp[i+1][j] %= mod

    print(dp[n][3000])

=======
Suggestion 2

def solve():
    mod = 998244353
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    dp = [[0 for i in range(3001)] for j in range(n)]
    for i in range(a[0], b[0] + 1):
        dp[0][i] = 1
    for i in range(1, n):
        for j in range(3001):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
            if j > b[i]:
                dp[i][j] -= dp[i - 1][j - b[i] - 1]
            if j - a[i] - 1 >= 0:
                dp[i][j] -= dp[i - 1][j - a[i] - 1]
            dp[i][j] %= mod
    print(dp[n - 1][3000])

=======
Suggestion 3

def get_input():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    return n,a,b

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    mod = 998244353
    dp = [[0 for _ in range(3001)] for _ in range(3001)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(a[i], b[i] + 1):
            for k in range(j + 1):
                dp[i + 1][k] += dp[i][k]
                dp[i + 1][k] %= mod
            for k in range(j, -1, -1):
                dp[i + 1][j] += dp[i][k]
                dp[i + 1][j] %= mod
    print(sum(dp[n]) % mod)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 1
    for i in range(n):
        ans *= max(0, b[i] - a[i] + 1)
        ans %= 998244353
    print(ans)

=======
Suggestion 6

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 1
    for i in range(N):
        ans *= max(0, B[i] - A[i] + 1)
        ans %= 998244353
    print(ans)

=======
Suggestion 7

def func(a,b):
    if a==b:
        return 1
    elif a>b:
        return 0
    else:
        return sum([func(i,b) for i in range(a,b+1)])%998244353

n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
print(sum([func(a[i],b[i]) for i in range(n)])%998244353)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    mod = 998244353
    ans = 1
    for i in range(n):
        ans *= max(0, b[i] - a[i] + 1)
        ans %= mod
    print(ans)

=======
Suggestion 9

def solve(n, a, b):
    mod = 998244353
    dp = [[0 for i in range(3001)] for j in range(n)]
    for i in range(a[0], b[0] + 1):
        dp[0][i] = 1
    for i in range(1, n):
        for j in range(3001):
            dp[i][j] = dp[i - 1][j]
        for j in range(a[i], b[i] + 1):
            dp[i][j] += dp[i][j - 1]
            dp[i][j] %= mod
    return dp[n - 1][b[n - 1]]

=======
Suggestion 10

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = 998244353
    dp = [[0 for i in range(3001)] for j in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(A[i-1], B[i-1]+1):
            dp[i][j] = dp[i-1][j]
        for j in range(1, 3001):
            dp[i][j] += dp[i][j-1]
            dp[i][j] %= MOD
    print(dp[N][3000])

solve()
