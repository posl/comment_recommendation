def solve():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    ans = 0
    from heapq import heappop, heappush
    h = []
    for i in range(1, M+1):
        while AB and AB[0][0] <= i:
            a, b = AB.pop(0)
            heappush(h, -b)
        if h:
            ans -= heappop(h)
    print(ans)

if __name__ == '__main__':
    solve()