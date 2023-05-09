def solve():
    N, M = map(int, input().split())
    AB = sorted([list(map(int, input().split())) for _ in range(N)])
    ans = 0
    i = 0
    import heapq
    h = []
    for day in range(1, M+1):
        while i < N and AB[i][0] <= day:
            heapq.heappush(h, -AB[i][1])
            i += 1
        if h:
            ans -= heapq.heappop(h)
    return ans

if __name__ == '__main__':
    solve()