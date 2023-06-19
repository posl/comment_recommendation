def main():
    from collections import Counter
    from heapq import heappush, heappop
    import sys
    input = sys.stdin.readline
    q = int(input())
    s = []
    c = Counter()
    hq = []
    for _ in range(q):
        query = input().split()
        if query[0] == '1':
            x = int(query[1])
            s.append(x)
            c[x] += 1
        elif query[0] == '2':
            x = int(query[1])
            m = min(int(query[2]), c[x])
            c[x] -= m
            for _ in range(m):
                heappush(hq, x)
        else:
            while hq and c[hq[0]] == 0:
                heappop(hq)
            print(hq[-1] - hq[0])

if __name__ == '__main__':
    main()