def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    #print(AB)
    import heapq
    heap = []
    ans = 0
    for i in range(1, M+1):
        while AB and AB[0][0] == i:
            a, b = AB.pop(0)
            heapq.heappush(heap, -b)
        if heap:
            ans -= heapq.heappop(heap)
    print(ans)
