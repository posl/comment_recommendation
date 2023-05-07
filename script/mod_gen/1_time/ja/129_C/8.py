def main():
    N, M = map(int, input().split())
    a = [int(input()) for _ in range(M)]
    a.append(N)
    a.append(0)
    a.sort()
    a.reverse()
    mod = 10 ** 9 + 7
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(N):
        if i + 1 in a:
            continue
        dp[i + 1] = dp[i] + dp[i - 1]
        dp[i + 1] %= mod
    print(dp[N])

if __name__ == '__main__':
    main()