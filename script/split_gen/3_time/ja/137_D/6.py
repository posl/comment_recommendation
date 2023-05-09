def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    ans = 0
    import heapq
    heap = []
    for i in range(1, M+1):
        for a, b in AB:
            if a == i:
                heapq.heappush(heap, -b)
            else:
                break
        if heap:
            ans -= heapq.heappop(heap)
    print(ans)
