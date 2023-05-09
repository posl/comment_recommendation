def main():
    N, M = map(int, input().split())
    jobs = [list(map(int, input().split())) for _ in range(N)]
    jobs.sort(key=lambda x: x[1], reverse=True)
    jobs.sort(key=lambda x: x[0])
    dp = [0] * (M + 1)
    for i in range(N):
        a, b = jobs[i][0], jobs[i][1]
        for j in range(M, -1, -1):
            if j + a <= M:
                dp[j + a] = max(dp[j + a], dp[j] + b)
    print(max(dp))

if __name__ == '__main__':
    main()