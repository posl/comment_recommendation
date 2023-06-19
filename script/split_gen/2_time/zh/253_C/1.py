def solve():
    from collections import defaultdict
    from heapq import heappush, heappop
    import sys
    input = sys.stdin.readline
    q = int(input())
    s = []
    sdict = defaultdict(int)
    smin = []
    smax = []
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            s.append(query[1])
            sdict[query[1]] += 1
        elif query[0] == 2:
            x, c = query[1], query[2]
            while c > 0:
                if sdict[x] == 0:
                    break
                sdict[x] -= 1
                c -= 1
            if sdict[x] == 0:
                sdict.pop(x)
        else:
            while sdict[s[0]] == 0:
                s.pop(0)
            while sdict[s[-1]] == 0:
                s.pop()
            print(s[-1] - s[0])
