def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    dp = [-1] * (N + 1)
    dp[0] = 0
    for i in range(N + 1):
        for a in A:
            if i - a >= 0:
                dp[i] = max(dp[i], dp[i - a] * 10 + a)
    print(dp[N])

if __name__ == '__main__':
    main()