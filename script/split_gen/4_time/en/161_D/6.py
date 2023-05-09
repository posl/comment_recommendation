def solve(K):
    # write your code in Python 3.6
    import heapq
    q = []
    for i in range(1,10):
        heapq.heappush(q, i)
    for i in range(K-1):
        v = heapq.heappop(q)
        if v%10 != 0:
            heapq.heappush(q, 10*v+(v%10)-1)
        heapq.heappush(q, 10*v+(v%10))
        if v%10 != 9:
            heapq.heappush(q, 10*v+(v%10)+1)
    return heapq.heappop(q)
