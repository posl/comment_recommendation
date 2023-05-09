def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [-1] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        for a in A:
            if i >= a and dp[i - a] != -1:
                dp[i] = max(dp[i], dp[i - a] * 10 + a)
    print(dp[-1])

if __name__ == '__main__':
    main()