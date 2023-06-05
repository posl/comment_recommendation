def solve():
    from collections import Counter
    from heapq import heappush, heappop
    from bisect import bisect_left, bisect_right
    import sys
    input = sys.stdin.readline
    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]
    # 1回目のクエリの処理
    c = Counter()
    minheap = []
    maxheap = []
    for q in queries:
        if q[0] == 1:
            c[q[1]] += 1
            heappush(minheap, q[1])
            heappush(maxheap, -q[1])
        elif q[0] == 2:
            x, c = q[1], q[2]
            while c > 0 and c[x] > 0:
                c[x] -= 1
                c -= 1
        else:
            break
    # 2回目のクエリの処理
    minheap2 = []
    maxheap2 = []
    for q in queries:
        if q[0] == 1:
            c[q[1]] += 1
            heappush(minheap2, q[1])
            heappush(maxheap2, -q[1])
        elif q[0] == 2:
            x, c = q[1], q[2]
            while c > 0 and c[x] > 0:
                c[x] -= 1
                c -= 1
        else:
            break
    ans = []
    for q in queries:
        if q[0] == 1:
            c[q[1]] += 1
            heappush(minheap2, q[1])
            heappush(maxheap2, -q[1])
        elif q[0] == 2:
            x, c = q[1], q[2]
            while c > 0 and c[x] > 0:
                c[x] -= 1
                c -= 1
        else:
            ans.append(-maxheap2[0] - minheap2[0])
    print('\n'.join(map(str, ans)))
solve()
