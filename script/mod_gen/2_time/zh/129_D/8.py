def main():
    N, M = map(int, input().split())
    a = []
    for i in range(M):
        a.append(int(input()))
    a.append(N)
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(N):
        if dp[i] == 0:
            continue
        for j in range(M + 1):
            if i + a[j] > N:
                break
            dp[i + a[j]] = (dp[i + a[j]] + dp[i]) % 1000000007
    print(dp[N])

if __name__ == '__main__':
    main()