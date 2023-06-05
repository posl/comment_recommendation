def main():
    n,m = map(int,input().split())
    jobs = []
    for i in range(n):
        a,b = map(int,input().split())
        jobs.append((a,b))
    jobs.sort(key=lambda x:x[0])
    #print(jobs)
    #dp[i][j]表示前i个工作中，完成j个工作的最大奖励
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]+jobs[i-1][1]) if j>=jobs[i-1][0] else dp[i-1][j]
    print(dp[n][m])
