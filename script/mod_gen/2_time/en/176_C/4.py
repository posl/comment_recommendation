def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        dp[i] = max(dp[i - 1], A[i])
    ans = 0
    for i in range(1, N + 1):
        ans += dp[i] - A[i]
    print(ans)

if __name__ == '__main__':
    main()