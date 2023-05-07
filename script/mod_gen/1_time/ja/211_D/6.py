def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    MOD = 10 ** 9 + 7
    path = [[] for _ in range(N)]
    for a, b in AB:
        path[a - 1].append(b - 1)
        path[b - 1].append(a - 1)
    # print(path)
    dp = [0] * N
    dp[0] = 1
    for i in range(N):
        for j in path[i]:
            dp[j] += dp[i]
            dp[j] %= MOD
    print(dp[N - 1])

if __name__ == '__main__':
    main()