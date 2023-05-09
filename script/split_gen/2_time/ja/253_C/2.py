def main():
    import sys
    from heapq import heappush, heappop
    input = sys.stdin.readline
    Q = int(input())
    hq = []
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            heappush(hq, query[1])
        elif query[0] == 2:
            for _ in range(min(query[2], hq.count(query[1]))):
                hq.remove(query[1])
        else:
            print(heappop(hq) - heappop(hq))
            heappush(hq, heappop(hq))
            heappush(hq, heappop(hq))
