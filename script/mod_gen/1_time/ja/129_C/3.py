def main():
    N, M = map(int, input().split())
    A = [0] + [int(input()) for _ in range(M)] + [N+1]
    A.sort()
    MOD = 10**9 + 7
    dp = [0] * (N+1)
    dp[0] = 1
    for i in range(1, N+1):
        if i in A:
            continue
        dp[i] = dp[i-1] + dp[i-2]
        dp[i] %= MOD
    print(dp[N])

if __name__ == '__main__':
    main()