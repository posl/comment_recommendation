def main():
    N, M = map(int, input().split())
    jobs = []
    for i in range(N):
        A, B = map(int, input().split())
        jobs.append((A, B))
    jobs.sort(key=lambda x: x[0])
    ans = 0
    idx = 0
    for _ in range(M):
        while idx < N and jobs[idx][0] <= _ + 1:
            heapq.heappush(q, -jobs[idx][1])
            idx += 1
        if q:
            ans += -heapq.heappop(q)
    print(ans)

if __name__ == '__main__':
    main()