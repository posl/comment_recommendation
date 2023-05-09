def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    matchsticks = [2, 5, 5, 4, 5, 6, 3, 7, 6]
    dp = [-1] * (N+1)
    dp[0] = 0
    for i in range(N):
        for j in A:
            if i + matchsticks[j-1] <= N:
                dp[i+matchsticks[j-1]] = max(dp[i+matchsticks[j-1]], dp[i]*10+j)
    print(dp[N])

if __name__ == '__main__':
    main()