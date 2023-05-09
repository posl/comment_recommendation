def main():
    N, M = map(int, input().split())
    broken = [False] * (N + 1)
    for i in range(M):
        broken[int(input())] = True
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        if broken[i]:
            continue
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
    print(dp[N])

if __name__ == '__main__':
    main()