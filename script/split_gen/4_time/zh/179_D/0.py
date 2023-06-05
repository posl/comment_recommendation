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
