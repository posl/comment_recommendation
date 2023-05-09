def main():
    N, M = map(int, input().split())
    job = []
    for i in range(N):
        A, B = map(int, input().split())
        job.append([A, B])
    job.sort(key=lambda x: x[0])
    #print(job)
    ans = 0
    import heapq
    hq = []
    for i in range(M):
        for j in range(N):
            if job[j][0] == i+1:
                heapq.heappush(hq, -job[j][1])
        if hq:
            ans += -heapq.heappop(hq)
    print(ans)
