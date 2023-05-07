def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [0] * (n + 1)
    for i in range(n):
        if dp[i] == 0:
            for j in range(k):
                if i + a[j] > n:
                    break
                dp[i + a[j]] = 1
    if dp[n] == 1:
        print("Takahashi")
    else:
        print("Aoki")
