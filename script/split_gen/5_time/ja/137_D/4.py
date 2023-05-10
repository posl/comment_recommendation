def solve():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB = sorted(AB, key=lambda x: x[0])
    i = 0
    ans = 0
    for _ in range(M):
        while i < N and AB[i][0] <= _ + 1:
            heapq.heappush(h, -AB[i][1])
            i += 1
        if h:
            ans -= heapq.heappop(h)
    print(ans)
h = []
solve()
