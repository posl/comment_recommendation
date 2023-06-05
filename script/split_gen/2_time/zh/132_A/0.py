def solve():
    N = int(input())
    jobs = []
    for i in range(N):
        a,b = map(int,input().split())
        jobs.append([a,b])
    jobs = sorted(jobs,key=lambda x:x[1])
    time = 0
    for i in range(N):
        time += jobs[i][0]
        if time > jobs[i][1]:
            print("No")
            return
    print("Yes")
    return
