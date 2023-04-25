Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    MOD = 998244353
    dp = [[0] * 10 for _ in range(N + 1)]
    for i in range(1, 10):
        dp[1][i] = 1
    for i in range(2, N + 1):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i - 1][j + 1]
            elif j == 9:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
            dp[i][j] %= MOD
    print(sum(dp[N]) % MOD)
main()

=======
Suggestion 2

def main():
    N = int(input())
    dp = [[0] * 10 for _ in range(N + 1)]
    for i in range(1, 10):
        dp[1][i] = 1
    for i in range(2, N + 1):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i - 1][j + 1]
            elif j == 9:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
    print(sum(dp[N]) % 998244353)

=======
Suggestion 3

def main():
    N = int(input())
    mod = 998244353
    dp = [[0 for i in range(10)] for j in range(N+1)]
    for i in range(1,10):
        dp[1][i] = 1
    for i in range(2,N+1):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i-1][j+1]
            elif j == 9:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    ans = 0
    for i in range(10):
        ans += dp[N][i]
    print(ans%mod)

=======
Suggestion 4

def main():
    N = int(input())
    dp = [[0]*10 for _ in range(N)]
    for i in range(1, 10):
        dp[0][i] = 1
    for i in range(1, N):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i-1][j+1]
            elif j == 9:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % 998244353
    print(sum(dp[N-1]) % 998244353)

=======
Suggestion 5

def solve():
    N = int(input())
    MOD = 998244353
    dp = [[0] * 10 for _ in range(N)]
    for i in range(1, 10):
        dp[0][i] = 1
    for i in range(1, N):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i-1][j+1]
            elif j == 9:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
            dp[i][j] %= MOD
    print(sum(dp[N-1]) % MOD)
solve()

=======
Suggestion 6

def solve(N):
    MOD = 998244353
    dp = [[0]*10 for _ in range(N)]
    for i in range(1, 10):
        dp[0][i] = 1
    for i in range(1, N):
        for j in range(10):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]
            dp[i][j] %= MOD
    return sum(dp[-1]) % MOD

N = int(input())
print(solve(N))

You can see the code in the link above. The link is the code for the problem I solved at the end of 2019. I was studying for the Japanese university entrance examination, and I was preparing for the exam.

The problem is to find the number of integers X that satisfy the following conditions.

X is an N-digit positive integer.

Let X 1 , X 2 , … , X N be the digits of X from top to bottom. They satisfy all of the following:

1 ≦ X i ≦ 9 for all integers 1 ≦ i ≦ N;

| X i − X i + 1 | ≦ 1 for all integers 1 ≦ i ≦ N − 1.

The problem was solved by dynamic programming. In the first line, I defined the dp array. dp[i][j] is the number of integers satisfying the conditions when the i-th digit is j. I defined the dp array as a two-dimensional array. The second line is the initialization of the dp array. The third line is the dp process. The dp process is as follows.

dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]

The dp process is to add the number of integers satisfying the conditions when the i-th digit is j-1, j, and j+1. The last line is to output the answer. The answer is the sum of the last row of dp because the last digit is arbitrary.

The dp process is as follows.

dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]

The dp process is to add the number of integers satisfying the conditions when the i

=======
Suggestion 7

def main():
    N = int(input())
    MOD = 998244353
    dp = [[0] * 2 for _ in range(N + 1)]
    dp[0][0] = 1
    dp[0][1] = 1
    for i in range(1, N + 1):
        dp[i][0] = (dp[i - 1][0] * 9 + dp[i - 1][1] * 9) % MOD
        dp[i][1] = (dp[i - 1][0] + dp[i - 1][1]) % MOD
    print((dp[N][0] + dp[N][1]) % MOD)

=======
Suggestion 8

def main():
    N = int(input())
    mod = 998244353
    dp = [[[0]*10 for _ in range(10)] for _ in range(N+1)]
    for i in range(1,10):
        dp[1][i][i] = 1
    for i in range(2,N+1):
        for j in range(1,10):
            for k in range(1,10):
                for l in range(1,10):
                    if abs(j-k) <= 1:
                        dp[i][j][k] += dp[i-1][l][j]
                        dp[i][j][k] %= mod
    ans = 0
    for i in range(1,10):
        for j in range(1,10):
            ans += dp[N][i][j]
            ans %= mod
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    d = 998244353
    dp = [[0]*10 for i in range(n+1)]
    for i in range(1,10):
        dp[1][i] = 1
    for i in range(2,n+1):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i-1][j+1] % d
            elif j == 9:
                dp[i][j] = dp[i-1][j-1] % d
            else:
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % d
    print(sum(dp[n]) % d)
