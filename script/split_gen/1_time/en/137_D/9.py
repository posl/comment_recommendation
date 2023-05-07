def main():
    from bisect import bisect_left
    import heapq
    N, M = map(int, input().split())
    A, B = [], []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A, B = zip(*sorted(zip(A, B), key=lambda x: x[0]))
    B = list(B)
    A = list(A)
    # print(A)
    # print(B)
    ans = 0
    heap = []
    for i in range(M):
        # print(i, ans, heap)
        idx = bisect_left(A, i+1)
        for j in range(idx):
            heapq.heappush(heap, -B[j])
        if heap:
            ans += -heapq.heappop(heap)
    print(ans)
