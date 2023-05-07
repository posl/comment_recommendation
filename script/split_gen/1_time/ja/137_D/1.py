def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    #print(AB)
    import heapq
    q = []
    ans = 0
    for i in range(M):
        while AB and AB[0][0] == i+1:
            a, b = AB.pop(0)
            heapq.heappush(q, -b)
        if q:
            ans -= heapq.heappop(q)
    print(ans)
