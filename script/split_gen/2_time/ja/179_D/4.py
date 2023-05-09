def main():
    n, k = map(int, input().split())
    l = []
    r = []
    for i in range(k):
        l1, r1 = map(int, input().split())
        l.append(l1)
        r.append(r1)
    mod = 998244353
    dp = [0] * (n + 1)
    dp[1] = 1
    s = [0] * (n + 1)
    s[1] = 1
    for i in range(2, n + 1):
        for j in range(k):
            if i - l[j] < 0:
                continue
            dp[i] += s[i - l[j]]
            dp[i] %= mod
            if i - r[j] - 1 >= 0:
                dp[i] -= s[i - r[j] - 1]
                dp[i] %= mod
        s[i] = s[i - 1] + dp[i]
        s[i] %= mod
    print(dp[n])
