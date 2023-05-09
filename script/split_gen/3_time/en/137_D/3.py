def main():
    N, M = map(int, input().split())
    jobs = []
    for i in range(N):
        A, B = map(int, input().split())
        jobs.append([A, B])
    jobs.sort()
    jobs.reverse()
    days = [0] * (M + 1)
    for i in range(N):
        for j in range(M - 1, -1, -1):
            if days[j] != 0:
                if j + jobs[i][0] < M + 1:
                    if days[j + jobs[i][0]] == 0:
                        days[j + jobs[i][0]] = days[j] + jobs[i][1]
                    else:
                        days[j + jobs[i][0]] = max(days[j + jobs[i][0]], days[j] + jobs[i][1])
            elif j + jobs[i][0] < M + 1:
                days[j + jobs[i][0]] = jobs[i][1]
    print(max(days))
