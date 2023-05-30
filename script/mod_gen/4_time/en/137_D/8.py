def solve():
    n, m = map(int, input().split())
    jobs = [tuple(map(int, input().split())) for i in range(n)]
    jobs.sort(key=lambda x: x[0])
    import heapq
    heap = []
    ans = 0
    for d in range(1, m+1):
        while jobs and jobs[0][0] == d:
            heapq.heappush(heap, -jobs[0][1])
            jobs.pop(0)
        if heap:
            ans += -heapq.heappop(heap)
    print(ans)
solve()
