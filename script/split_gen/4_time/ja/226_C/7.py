def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    import heapq
    h = []
    for i in range(N):
        heapq.heappush(h, (0, i))
    while h:
        t, i = heapq.heappop(h)
        if t < A[i][0]:
            t = A[i][0]
        t += A[i][1]
        for j in range(2, A[i][1]+2):
            heapq.heappush(h, (t, A[i][j]-1))
        if i == N-1:
            print(t)
            return
