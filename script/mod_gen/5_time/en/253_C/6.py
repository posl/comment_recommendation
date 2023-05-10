def main():
    from sys import stdin
    from collections import Counter
    from heapq import heappop, heappush
    input = stdin.buffer.readline
    N = int(input())
    S = []
    Smin = []
    Smax = []
    Ssum = 0
    Ssum_min = 0
    Ssum_max = 0
    count = Counter()
    for _ in range(N):
        query = input().split()
        if query[0] == b'1':
            x = int(query[1])
            Ssum += x
            heappush(S, x)
            count[x] += 1
            if len(Smin) == 0 or x <= Smin[0]:
                heappush(Smin, x)
                Ssum_min += x
            else:
                heappush(Smax, -x)
                Ssum_max += x
        elif query[0] == b'2':
            x = int(query[1])
            c = int(query[2])
            while c > 0:
                if count[x] == 0:
                    break
                if x <= Smin[0]:
                    heappop(Smin)
                    Ssum_min -= x
                else:
                    heappop(Smax)
                    Ssum_max -= x
                heappop(S)
                Ssum -= x
                count[x] -= 1
                c -= 1
        else:
            print(-Smin[0] + Ssum - Ssum_min + Ssum_max)
    return

if __name__ == '__main__':
    main()