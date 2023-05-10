def solve():
    N, M = map(int, input().split())
    jobs = []
    for i in range(N):
        A, B = map(int, input().split())
        jobs.append((A, B))
    jobs.sort()
    jobs.reverse()
    days = []
    for i in range(M):
        days.append([])
    for i in range(N):
        A, B = jobs[i]
        if (M - A) >= 0:
            days[M - A].append(B)
    import heapq
    heap = []
    heapq.heapify(heap)
    ans = 0
    for i in range(M):
        for j in range(len(days[i])):
            heapq.heappush(heap, days[i][j])
        if len(heap) > 0:
            ans += heapq.heappop(heap)
    print(ans)
solve()
