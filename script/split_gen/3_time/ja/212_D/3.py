def main():
    import heapq
    import sys
    input = sys.stdin.readline
    Q = int(input())
    query = [input().split() for _ in range(Q)]
    heap = []
    add = 0
    for p, x in query:
        if p == '1':
            heapq.heappush(heap, int(x) - add)
        elif p == '2':
            add += int(x)
        else:
            print(heapq.heappop(heap) + add)
