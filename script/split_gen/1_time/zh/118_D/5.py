def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    dp = [0] * (n + 1)
    for i in range(m):
        for j in range(n + 1):
            if j >= a[i]:
                dp[j] = max(dp[j], dp[j - a[i]] * 10 + a[i])
    print(dp[n])
