def main():
    import heapq
    import sys
    input = sys.stdin.readline
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    heap = []
    add = 0
    for q in query:
        if q[0] == 1:
            heapq.heappush(heap, q[1] - add)
        elif q[0] == 2:
            add += q[1]
        else:
            print(heapq.heappop(heap) + add)
