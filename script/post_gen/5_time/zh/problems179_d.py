Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def get_input():
    n, k = map(int, input().split())
    l_r = []
    for i in range(k):
        l_r.append(list(map(int, input().split())))
    return n, k, l_r

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    left = []
    right = []
    for i in range(k):
        a,b = map(int,input().split())
        left.append(a)
        right.append(b)
    mod = 998244353
    dp = [0]*(n+1)
    dp[1] = 1
    for i in range(1,n):
        dp[i+1] = (dp[i+1]+dp[i])%mod
        for j in range(k):
            if i+left[j] <= n:
                dp[i+left[j]] = (dp[i+left[j]]+dp[i])%mod
            if i+right[j]+1 <= n:
                dp[i+right[j]+1] = (dp[i+right[j]+1]-dp[i]+mod)%mod
    print(dp[n])

=======
Suggestion 4

def main():
    n,k = map(int,input().split())
    lr = []
    for i in range(k):
        lr.append(list(map(int,input().split())))
    print(n,k,lr)

=======
Suggestion 5

def solve():
    # 状态转移方程
    # dp[i] = sum(dp[i - L[j]] for j in range(k) if L[j] <= i <= R[j])
    # dp[i] = dp[i - 2] + dp[i - 3] + dp[i - 4] + dp[i - 5] + dp[i - 6]
    # dp[i] = dp[i - 3] + dp[i - 5] + dp[i - 6] + dp[i - 7] + dp[i - 8]
    # dp[i] = dp[i - 5] + dp[i - 6] + dp[i - 7] + dp[i - 8] + dp[i - 9] + dp[i - 10]
    # dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4] + dp[i - 5] + dp[i - 6]
    # dp[i] = dp[i - 1] + dp[i - 3] + dp[i - 5] + dp[i - 6] + dp[i - 7] + dp[i - 8]
    # dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 5] + dp[i - 6] + dp[i - 7]
    # dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4] + dp[i - 5] + dp[i - 6]
    # dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4] + dp[i - 5] + dp[i - 6]
    # dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4] + dp[i - 5] + dp[i - 6]
    # dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4] + dp[i - 5] + dp[i - 6]
    # dp[i

=======
Suggestion 6

def solve(n, k, l, r):
    ans = 0
    dp = [0 for _ in range(n + 1)]
    dp[1] = 1
    for i in range(1, n + 1):
        for j in range(k):
            if i + l[j] <= n:
                dp[i + l[j]] += dp[i]
                dp[i + l[j]] %= 998244353
            if i + r[j] + 1 <= n:
                dp[i + r[j] + 1] -= dp[i]
                dp[i + r[j] + 1] %= 998244353
    for i in range(1, n + 1):
        dp[i] += dp[i - 1]
        dp[i] %= 998244353
    return dp[n]

n, k = map(int, input().split())
l = []
r = []
for i in range(k):
    a, b = map(int, input().split())
    l.append(a)
    r.append(b)
print(solve(n, k, l, r))

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]

    mod = 998244353
    dp = [0] * (N+1)

    dp[1] = 1
    dpsum = [0] * (N+1)
    dpsum[1] = 1

    for i in range(2, N+1):
        for j in range(K):
            l = max(0, i - LR[j][1])
            r = i - LR[j][0]

            if r < 0:
                continue

            dp[i] += dpsum[r] - dpsum[l-1]

        dp[i] %= mod
        dpsum[i] = dpsum[i-1] + dp[i]

    print(dp[N])
