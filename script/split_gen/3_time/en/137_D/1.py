def main():
    N, M = map(int, input().split())
    jobs = []
    for _ in range(N):
        A, B = map(int, input().split())
        jobs.append((A, B))
    jobs.sort()
    import heapq
    heap = []
    heapq.heapify(heap)
    score = 0
    idx = 0
    for d in range(M):
        while idx < N and jobs[idx][0] == d + 1:
            heapq.heappush(heap, -jobs[idx][1])
            idx += 1
        if len(heap) > 0:
            score += -heapq.heappop(heap)
    print(score)
