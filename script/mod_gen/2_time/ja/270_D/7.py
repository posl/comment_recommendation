def main():
    import sys
    readline = sys.stdin.readline
    N, K = map(int, readline().split())
    A = list(map(int, readline().split()))
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        for j in range(K):
            if i - A[j] < 0:
                break
            if dp[i - A[j]] == 0:
                dp[i] = 1
                break
    print(dp[N] * "Takahashi" or "Aoki")

if __name__ == '__main__':
    main()