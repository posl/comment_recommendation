Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    MOD = 998244353
    ans = 1
    for i in range(n):
        ans *= max(0, b[i] - a[i] + 1)
        ans %= MOD
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
        ans = ans * (min(b[i], max(a[i], b[i - 1])) - a[i] + 1) % mod
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    mod = 998244353
    dp = [[0 for i in range(3010)] for j in range(3010)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(a[i], b[i] + 1):
            dp[i + 1][j] = (dp[i + 1][j - 1] + dp[i][j]) % mod
    print(dp[n][b[n - 1]])

=======
Suggestion 4

def get_input():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    return n, a, b

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    mod = 998244353
    dp = [[0] * 3001 for _ in range(3001)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(a[i], b[i] + 1):
            dp[i + 1][j] = (dp[i + 1][j - 1] + dp[i][j]) % mod
    print(dp[n][b[n - 1]])

=======
Suggestion 6

def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 1
    for i in range(N):
        ans *= max(0, b[i] - a[i] + 1)
        ans %= 998244353
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = 998244353

    #C = (c_1, c_2, ..., c_N)
    #a_i ≦ c_i ≦ b_i，对于每一个i（1 ≦ i ≦ N）。
    #找出能成为C的序列的数量，模数为998244353。

    #dp[i][j] = (a_i ≦ c_i ≦ j)的数量
    dp = [[0 for _ in range(3001)] for _ in range(3001)]
    for i in range(N):
        for j in range(A[i], B[i]+1):
            dp[i][j] = 1
    for i in range(N):
        for j in range(1, 3001):
            if i == 0:
                dp[i][j] += dp[i][j-1]
            else:
                dp[i][j] += dp[i-1][j] + dp[i][j-1]
            dp[i][j] %= MOD
    print(dp[N-1][3000])
    return

main()

=======
Suggestion 8

def main():
    pass

=======
Suggestion 9

def solve(N, A, B):
    # 请在这里编写代码
    return 0

=======
Suggestion 10

def problem222_d():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    mod = 998244353
    ans = 1
    for i in range(n):
        ans *= max(b[i] - a[i] + 1, 0)
        ans %= mod
    print(ans)
problem222_d()
