def main():
    N, M = map(int, input().split())
    jobs = []
    for _ in range(N):
        jobs.append(list(map(int, input().split())))
    jobs.sort(key=lambda x: x[0])
    #print(jobs)
    i = 0
    reward = 0
    days = 0
    while days < M:
        if i >= N:
            break
        if days + jobs[i][0] <= M:
            reward += jobs[i][1]
            days += jobs[i][0]
        else:
            break
        i += 1
    print(reward)
