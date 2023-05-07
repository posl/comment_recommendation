def main():
    import sys
    from heapq import heappush, heappop, heapify
    readline = sys.stdin.readline
    write = sys.stdout.write
    Q = int(readline())
    heap = []
    heapify(heap)
    add = 0
    for _ in range(Q):
        query = readline().split()
        if query[0] == '1':
            heappush(heap, int(query[1]) - add)
        elif query[0] == '2':
            add += int(query[1])
        else:
            write(str(heappop(heap) + add) + '
')
    return
