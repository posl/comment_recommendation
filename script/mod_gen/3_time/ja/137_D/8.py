def main():
    N, M = map(int, input().split())
    jobs = [list(map(int, input().split())) for _ in range(N)]
    jobs.sort()
    jobs.append([M+1, 0])
    ans = 0
    dp = [0] * (M+1)
    for i in range(M):
        dp[i+1] = max(dp[i], dp[i+1])
        if jobs[0][0] == i+1:
            dp[i+1] = max(dp[i+1], jobs[0][1])
            jobs.pop(0)
        dp[i+jobs[0][0]] = max(dp[i+jobs[0][0]], dp[i] + jobs[0][1])
    print(dp[M])

if __name__ == '__main__':
    main()