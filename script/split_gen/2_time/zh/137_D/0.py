def solve():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    import heapq
    heap = []
    ans = 0
    j = 0
    for i in range(1, M + 1):
        while j < N and AB[j][0] == i:
            heapq.heappush(heap, -AB[j][1])
            j += 1
        if heap:
            ans += -heapq.heappop(heap)
    print(ans)
