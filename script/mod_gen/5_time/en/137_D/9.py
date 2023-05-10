def solve():
    N,M = map(int, input().split())
    AB = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x:x[0])
    AB.append([M+1,0])
    import heapq
    hq = []
    heapq.heapify(hq)
    i = 0
    ans = 0
    for day in range(1,M+1):
        while AB[i][0] == day:
            heapq.heappush(hq, -AB[i][1])
            i += 1
        if len(hq) > 0:
            ans += -heapq.heappop(hq)
    print(ans)

if __name__ == '__main__':
    solve()