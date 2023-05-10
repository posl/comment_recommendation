def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    match = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    dp = [-float('inf')] * (n+1)
    dp[0] = 0
    for i in range(n+1):
        for j in range(m):
            if i - match[a[j]] >= 0:
                dp[i] = max(dp[i], dp[i-match[a[j]]]*10 + a[j])
    print(dp[n])
