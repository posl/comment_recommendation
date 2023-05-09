def solve():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    ans = 0
    from heapq import heappush, heappop
    h = []
    j = 0
    for i in range(1, M+1):
        while j < N and AB[j][0] <= i:
            heappush(h, -AB[j][1])
            j += 1
        if len(h) > 0:
            ans += -heappop(h)
    print(ans)
solve()

if __name__ == '__main__':
    solve()