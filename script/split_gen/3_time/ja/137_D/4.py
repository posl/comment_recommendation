def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    AB.append([M+1, 0])
    ans = 0
    q = []
    for i in range(N+1):
        while q and q[0][0] < AB[i][0]:
            ans += heapq.heappop(q)[1]
        heapq.heappush(q, [-AB[i][1], AB[i][1]])
    print(ans)
