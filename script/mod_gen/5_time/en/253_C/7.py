def solve():
    import sys
    input = sys.stdin.readline
    from collections import defaultdict
    from bisect import bisect_right, bisect_left
    from heapq import heappop, heappush
    import heapq
    Q = int(input())
    q = []
    q2 = []
    q3 = []
    d = defaultdict(int)
    d2 = defaultdict(int)
    d3 = defaultdict(int)
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            heappush(q, query[1])
            d[query[1]] += 1
        elif query[0] == 2:
            while query[1] > 0:
                if len(q) == 0:
                    break
                x = heappop(q)
                if d[x] > 1:
                    d[x] -= 1
                    heappush(q, x)
                else:
                    d[x] -= 1
                query[1] -= 1
        else:
            while len(q) > 0:
                x = heappop(q)
                if d[x] > 1:
                    d[x] -= 1
                    heappush(q, x)
                else:
                    d[x] -= 1
                    d2[x] += 1
                    heappush(q2, x)
                    d3[x] += 1
                    heappush(q3, -x)
                    break
            print(-q3[0] - q2[0])

if __name__ == '__main__':
    solve()