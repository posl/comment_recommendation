def main():
    N,M = map(int, input().split())
    jobs = []
    for i in range(N):
        a,b = map(int, input().split())
        jobs.append((a,b))
    jobs.sort(key=lambda x:x[0])
    #print(jobs)
    ans = 0
    for i in range(N):
        if jobs[i][0] <= M:
            ans += jobs[i][1]
            M -= jobs[i][0]
        else:
            ans += jobs[i][1] * M
            break
    print(ans)
