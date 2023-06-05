Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    l = []
    r = []
    for i in range(k):
        a, b = map(int, input().split())
        l.append(a)
        r.append(b)
    dp = [0] * (n + 1)
    dp[1] = 1
    s = [0] * (n + 1)
    s[1] = 1
    for i in range(2, n + 1):
        for j in range(k):
            if i - l[j] >= 0:
                dp[i] += s[i - l[j]]
            if i - r[j] - 1 >= 0:
                dp[i] -= s[i - r[j] - 1]
        s[i] = (s[i - 1] + dp[i]) % 998244353
    print(dp[n] % 998244353)

=======
Suggestion 2

def solve():
    pass

=======
Suggestion 3

def get_input():
    n, k = map(int, input().split())
    lrs = []
    for i in range(k):
        lrs.append(list(map(int, input().split())))
    return n, k, lrs

=======
Suggestion 4

def solve(n, k, l, r):
    mod = 998244353
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        for j in range(k):
            if i - l[j] >= 1:
                dp[i] += dp[i - l[j]]
                dp[i] %= mod
            if i - r[j] - 1 >= 1:
                dp[i] -= dp[i - r[j] - 1]
                dp[i] %= mod
    return dp[n]

n, k = map(int, input().split())
l = []
r = []
for _ in range(k):
    li, ri = map(int, input().split())
    l.append(li)
    r.append(ri)
print(solve(n, k, l, r))

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]
    mod = 998244353

    dp = [0] * (N + 1)
    dp[1] = 1
    dp_sum = [0] * (N + 1)
    dp_sum[1] = 1

    for i in range(2, N + 1):
        for l, r in LR:
            li = max(i - r, 0)
            ri = i - l
            if ri < 0:
                continue
            dp[i] += dp_sum[ri] - dp_sum[li - 1]
            dp[i] %= mod
        dp_sum[i] = dp_sum[i - 1] + dp[i]
        dp_sum[i] %= mod
    print(dp[N])

=======
Suggestion 6

def solve(n, k, l, r):
    pass

=======
Suggestion 7

def main():
    pass

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    lr = [list(map(int, input().split())) for _ in range(k)]
    mod = 998244353
    dp = [0] * (n+1)
    dp[1] = 1
    dpsum = [0] * (n+1)
    dpsum[1] = 1
    for i in range(2, n+1):
        for l, r in lr:
            if i-l < 1:
                continue
            dp[i] += dpsum[i-l] - dpsum[max(0, i-r-1)]
            dp[i] %= mod
        dpsum[i] = dpsum[i-1] + dp[i]
        dpsum[i] %= mod
    print(dp[n])

=======
Suggestion 9

def main():
    return

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    LRs = [list(map(int, input().split())) for _ in range(K)]
    mod = 998244353
    dp = [0] * (N+1)
    dp[1] = 1
    for i in range(2, N+1):
        for l, r in LRs:
            if i-l >= 0:
                dp[i] += dp[i-l]
                dp[i] %= mod
            if i-r-1 >= 0:
                dp[i] -= dp[i-r-1]
                dp[i] %= mod
    print(dp[N])
