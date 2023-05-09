def main():
    N, M = map(int, input().split())
    jobs = []
    for _ in range(N):
        a, b = map(int, input().split())
        jobs.append((a, b))
    jobs.sort()
    from heapq import heappop, heappush
    q = []
    ans = 0
    j = 0
    for i in range(1, M + 1):
        while j < N and jobs[j][0] <= i:
            heappush(q, -jobs[j][1])
            j += 1
        if q:
            ans -= heappop(q)
    print(ans)
