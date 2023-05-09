def main():
    N, M = map(int, input().split())
    broken = [0] * (N + 1)
    for _ in range(M):
        broken[int(input())] = 1
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        if broken[i] == 1:
            continue
        if i - 1 >= 0:
            dp[i] += dp[i - 1]
        if i - 2 >= 0:
            dp[i] += dp[i - 2]
        dp[i] %= 10 ** 9 + 7
    print(dp[N])

if __name__ == '__main__':
    main()