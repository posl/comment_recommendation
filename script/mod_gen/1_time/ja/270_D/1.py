def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [False] * (n + 1)
    for i in range(1, n + 1):
        for j in range(k):
            if i - a[j] >= 0:
                dp[i] |= not dp[i - a[j]]
    print("Takahashi" if dp[n] else "Aoki")

if __name__ == '__main__':
    main()