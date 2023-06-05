def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    dp = [0 for i in range(n + 1)]
    for i in range(m):
        for j in range(a[i], n + 1):
            dp[j] = max(dp[j], dp[j - a[i]] * 10 + a[i])
    print(dp[n])
