def main():
    N, M = map(int, input().split())
    jobs = [list(map(int, input().split())) for _ in range(N)]
    jobs.sort(key=lambda x: x[1], reverse=True)
    dp = [0] * (M+1)
    for i in range(N):
        for j in range(M, 0, -1):
            if j >= jobs[i][0]:
                dp[j] = max(dp[j], dp[j-jobs[i][0]] + jobs[i][1])
    print(max(dp))

if __name__ == '__main__':
    main()