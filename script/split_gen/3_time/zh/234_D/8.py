def solve():
    from heapq import heappop, heappush
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    Q = []
    for i in range(K):
        heappush(Q, (-P[i], i))
    print(-Q[0][0])
    for i in range(K, N):
        heappush(Q, (-P[i], i))
        while Q[0][1] <= i - K:
            heappop(Q)
        print(-Q[0][0])
