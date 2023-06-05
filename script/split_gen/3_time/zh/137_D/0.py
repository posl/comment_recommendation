def solve():
    N, M = map(int, input().split())
    jobs = []
    for _ in range(N):
        A, B = map(int, input().split())
        jobs.append((A, B))
    jobs.sort(key=lambda x: x[0])
    import heapq
    h = []
    i = 0
    ans = 0
    for d in range(1, M + 1):
        while i < N and jobs[i][0] == d:
            heapq.heappush(h, -jobs[i][1])
            i += 1
        if h:
            ans += -heapq.heappop(h)
    print(ans)
solve()
