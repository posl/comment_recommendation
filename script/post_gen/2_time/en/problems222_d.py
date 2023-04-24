Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    ans = 1
    for i in range(N):
        ans *= max(0, B[i] - A[i] + 1)
        ans %= 998244353

    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    MOD = 998244353

    dp = [[0 for _ in range(3001)] for _ in range(N+1)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(A[i], B[i]+1):
            dp[i+1][j] = (dp[i+1][j-1] + dp[i][j]) % MOD

    print(dp[-1][-1])

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    mod = 998244353
    dp = [[0 for _ in range(3001)] for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(3001):
            if a[i] <= j <= b[i]:
                dp[i + 1][j] = dp[i][j]
            dp[i + 1][j] += dp[i + 1][j - 1]
            dp[i + 1][j] %= mod
    print(dp[n][3000])

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = 998244353

    dp = [[0 for i in range(3001)] for j in range(N)]
    dp[0][A[0]:B[0]+1] = [1 for i in range(A[0], B[0]+1)]
    for i in range(1, N):
        for j in range(3001):
            if j < A[i]:
                dp[i][j] = 0
            elif j > B[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = sum(dp[i-1][A[i]:j+1]) % MOD
    print(sum(dp[N-1]) % MOD)

=======
Suggestion 5

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = 998244353
    dp = [[0] * 3001 for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(B[i]+1):
            dp[i+1][j] = (dp[i+1][j-1] + dp[i][j]) % MOD
        for j in range(A[i]+1, B[i]+1):
            dp[i+1][j] = (dp[i+1][j] + dp[i+1][j-1]) % MOD
    print(dp[N][B[N-1]])

solve()

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = 998244353

    dp = [0 for _ in range(3001)]
    dp[0] = 1
    for i in range(N):
        tmp = [0 for _ in range(3001)]
        for j in range(A[i], B[i]+1):
            tmp[j] = dp[j]
        for j in range(1, 3001):
            tmp[j] += tmp[j-1]
            tmp[j] %= MOD
        dp = tmp
    print(dp[3000])
main()

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = 998244353
    dp = [[0 for _ in range(3010)] for _ in range(3010)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(A[i], B[i]+1):
            dp[i+1][j] = dp[i+1][j-1] + dp[i][j]
            dp[i+1][j] %= MOD
    print(dp[N][B[N-1]])

solve()

=======
Suggestion 8

def main():
    n = int(raw_input())
    a = map(int, raw_input().split())
    b = map(int, raw_input().split())
    MOD = 998244353
    dp = [[0 for i in xrange(3001)] for j in xrange(3001)]
    dp[0][0] = 1
    for i in xrange(n):
        for j in xrange(a[i], b[i] + 1):
            dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % MOD
            dp[i + 1][j] = (dp[i + 1][j] + dp[i + 1][j - 1]) % MOD
    print dp[n][b[n - 1]]

=======
Suggestion 9

def solve(arr1, arr2):
    mod = 998244353
    dp = [[0 for i in range(3001)] for j in range(3001)]
    dp[0][0] = 1
    for i in range(len(arr1)):
        for j in range(arr1[i], arr2[i] + 1):
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= mod
            dp[i + 1][j] += dp[i + 1][j - 1]
            dp[i + 1][j] %= mod
    return dp[len(arr1)][arr2[len(arr1) - 1]]

=======
Suggestion 10

def main():
    pass
