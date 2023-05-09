def solve():
    N, M = map(int, input().split())
    jobs = []
    for i in range(N):
        A, B = map(int, input().split())
        jobs.append((A, B))
    jobs.sort()
    ans = 0
    i = 0
    import heapq
    q = []
    for j in range(1, M+1):
        while i < N and jobs[i][0] <= j:
            heapq.heappush(q, -jobs[i][1])
            i += 1
        if len(q) > 0:
            ans -= heapq.heappop(q)
    print(ans)
