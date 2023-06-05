def main():
    from collections import Counter
    from heapq import heappop, heappush
    import sys
    input = sys.stdin.readline
    q = int(input())
    c = Counter()
    hq = []
    s = 0
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            x = query[1]
            c[x] += 1
            s += x
            heappush(hq, x)
        elif query[0] == 2:
            x, c_ = query[1], query[2]
            for _ in range(min(c_, c[x])):
                c[x] -= 1
                s -= x
        else:
            while c[hq[0]] == 0:
                heappop(hq)
            print(hq[-1] - hq[0])

if __name__ == '__main__':
    main()