def main():
    N, M = map(int,input().split())
    job = []
    for i in range(N):
        a, b = map(int,input().split())
        job.append((a,b))
    job.sort()
    dp = [0]*(M+1)
    for i in range(N):
        a, b = job[i]
        for j in reversed(range(M+1)):
            if j+a <= M:
                dp[j+a] = max(dp[j+a], dp[j]+b)
    print(max(dp))

if __name__ == '__main__':
    main()