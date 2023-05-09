def main():
    from heapq import heappop, heappush
    import sys
    input = sys.stdin.readline
    Q = int(input())
    heap = []
    ans = []
    offset = 0
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            heappush(heap, query[1] - offset)
        elif query[0] == 2:
            offset += query[1]
        else:
            ans.append(heappop(heap) + offset)
    print(*ans, sep='
')
    return
