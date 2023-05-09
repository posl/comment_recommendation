def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(k):
            if i - a[j] < 0:
                break
            if dp[i - a[j]] == 0:
                dp[i] = 1
                break
    if dp[n] == 0:
        print("Takahashi")
    else:
        print("Aoki")
