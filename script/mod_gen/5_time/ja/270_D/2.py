def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [False] * (N + 1)
    for i in range(N + 1):
        for j in range(K):
            if i - A[j] >= 0 and not dp[i - A[j]]:
                dp[i] = True
    print(sum(dp))

if __name__ == '__main__':
    main()