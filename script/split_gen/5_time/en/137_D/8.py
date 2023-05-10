def solve():
    N, M = map(int, input().split())
    jobs = []
    for i in range(N):
        jobs.append(tuple(map(int, input().split())))
    jobs.sort(key=lambda x: x[0])
    jobs.sort(key=lambda x: x[1], reverse=True)
    #print(jobs)
    days = [0] * (M+1)
    ans = 0
    for i in range(N):
        for j in range(jobs[i][0], 0, -1):
            if days[j] == 0:
                days[j] = jobs[i][1]
                ans += jobs[i][1]
                break
    #print(days)
    print(ans)
