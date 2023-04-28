Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    MOD = 998244353
    ans = 1
    for i in range(N):
        ans *= max(0, b[i] - a[i] + 1)
        ans %= MOD
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    MOD = 998244353

    dp = [[0 for _ in range(3001)] for _ in range(3001)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(A[i], B[i]+1):
            dp[i+1][j] = dp[i+1][j-1] + dp[i][j]
            dp[i+1][j] %= MOD
        for j in range(B[i]+1, 3001):
            dp[i+1][j] = dp[i+1][j-1]
    print(dp[N][3000])

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    dp = [[0 for j in range(3001)] for i in range(N)]

    for i in range(A[0], B[0]+1):
        dp[0][i] = 1

    for i in range(1, N):
        for j in range(A[i], B[i]+1):
            dp[i][j] = sum(dp[i-1][A[i-1]:j+1]) % 998244353

    print(sum(dp[N-1]) % 998244353)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    mod = 998244353

    dp = [0] * (b[0] + 1)
    for i in range(a[0], b[0] + 1):
        dp[i] = 1

    for i in range(1, n):
        dp_new = [0] * (b[i] + 1)
        for j in range(a[i], b[i] + 1):
            dp_new[j] = sum(dp[:j + 1]) % mod
        dp = dp_new

    print(sum(dp) % mod)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    dp = [[0] * 3001 for _ in range(n)]
    for i in range(a[0], b[0] + 1):
        dp[0][i] = 1
    for i in range(1, n):
        for j in range(a[i], b[i] + 1):
            dp[i][j] = sum(dp[i - 1][a[i - 1]:j + 1]) % 998244353
    print(sum(dp[-1]) % 998244353)

=======
Suggestion 6

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = 998244353
    dp = [0]*(B[0]+1)
    for i in range(A[0], B[0]+1):
        dp[i] = 1
    for i in range(1, N):
        for j in range(B[i]+1):
            dp[j] = dp[j] + dp[j-1]
            dp[j] %= MOD
        for j in range(A[i], B[i]+1):
            dp[j] += dp[j-1]
            dp[j] %= MOD
    print(dp[B[-1]])

solve()

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = 998244353

    dp = [[0] * (B[0]+1) for _ in range(N+1)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(B[i]+1):
            dp[i+1][j] += dp[i][j]
            dp[i+1][j] %= MOD
        for j in range(A[i], B[i]+1):
            dp[i+1][j] += dp[i+1][j-1]
            dp[i+1][j] %= MOD

    print(dp[N][B[N-1]])

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    result = 0
    for i in range(n):
        result += (b[i] - a[i] + 1)
        
    print(result % 998244353)

=======
Suggestion 9

def f(a,b):
    if a>b:
        return 0
    else:
        return b-a+1

=======
Suggestion 10

def read_int():
    return int(input())
