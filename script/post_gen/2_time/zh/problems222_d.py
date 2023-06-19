Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    #print(a)
    #print(b)
    c = [0]*n
    for i in range(n):
        c[i] = b[i] - a[i] + 1
    #print(c)
    ans = 1
    for i in range(n):
        ans *= c[i]
        ans %= 998244353
    print(ans)

=======
Suggestion 2

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
Suggestion 3

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = 998244353

    dp = [[0 for _ in range(3001)] for _ in range(3001)]
    for i in range(A[0], B[0] + 1):
        dp[0][i] = 1
    for i in range(1, N):
        for j in range(A[i], B[i] + 1):
            dp[i][j] = sum(dp[i - 1][A[i - 1]:j + 1]) % MOD
    print(sum(dp[N - 1]) % MOD)

=======
Suggestion 4

def solve():
    N = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    MOD = 998244353
    ans = 1
    for i in range(N):
        ans *= max(b[i] - a[i] + 1, 0)
        ans %= MOD
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    mod = 998244353

    dp = [[0] * (b[i] + 1) for i in range(n)]
    for i in range(a[0], b[0] + 1):
        dp[0][i] = 1

    for i in range(1, n):
        for j in range(a[i], b[i] + 1):
            dp[i][j] = sum(dp[i - 1][a[i - 1]:j + 1]) % mod

    print(sum(dp[n - 1]) % mod)

=======
Suggestion 6

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    mod = 998244353
    ans = 1
    for i in range(N):
        if A[i] > B[i]:
            print(0)
            return
        elif A[i] == B[i]:
            continue
        else:
            ans *= (B[i] - A[i] + 1)
            ans %= mod
    print(ans)

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = 998244353
    ans = 1
    for i in range(N):
        ans = ans * max(0, B[i] - A[i] + 1) % MOD
    print(ans)

solve()

=======
Suggestion 8

def main():
    pass

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # dp[i][j] = (dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]) + (b[j] - a[i] + 1)
    # dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + (b[j] - a[i] + 1)
    # dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + b[j] - a[i] + 1
    # dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + b[j] - a[i] + 1
    # dp[i][j] = dp[i-1][j] + dp[i][j-1] + b[j] - a[i] + 1 - dp[i-1][j-1]
    # dp[i][j] = dp[i-1][j] + dp[i][j-1] + b[j] - a[i] + 1 - dp[i-1][j-1]
    # dp[i][j] = dp[i-1][j] + dp[i][j-1] + b[j] - a[i] + 1 - dp[i-1][j-1]
    # dp[i][j] = dp[i-1][j] + dp[i][j-1] + b[j] - a[i] + 1 - dp[i-1][j-1]
    # dp[i][j] = dp[i-1][j] + dp[i][j-1] + b[j] - a[i] + 1 - dp[i-1][j-1]
    # dp[i][j] = dp[i-1][j] + dp[i][j-1] + b[j] - a[i] + 1 - dp[i-1][j-1]
    # dp[i][j] = dp[i-1][j] + dp[i][j-1]
