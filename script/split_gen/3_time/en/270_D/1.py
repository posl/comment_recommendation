def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(k):
            if i - a[j] >= 0:
                dp[i] = dp[i] or not dp[i - a[j]]
    print("Takahashi" if dp[n] else "Aoki")
