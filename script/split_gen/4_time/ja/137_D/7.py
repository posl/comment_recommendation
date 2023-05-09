def calc():
    n, m = map(int, input().split())
    jobs = []
    for i in range(n):
        a, b = map(int, input().split())
        jobs.append((a, b))
    jobs.sort()
    #print(jobs)
    ans = 0
    i = 0
    while m > 0:
        if i >= n:
            break
        if jobs[i][0] > m:
            break
        ans += jobs[i][1]
        m -= jobs[i][0]
        i += 1
    print(ans)
calc()
