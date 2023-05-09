def main():
    N, M = map(int, input().split())
    AB = []
    for i in range(N):
        A, B = map(int, input().split())
        AB.append([A, B])
    AB.sort(key=lambda x: x[0])
    ans = 0
    q = []
    for i in range(M):
        while q and q[0][0] < i:
            heapq.heappop(q)
        while AB and AB[0][0] == i + 1:
            heapq.heappush(q, [-AB[0][1], AB[0][1]])
            AB.pop(0)
        if q:
            ans += heapq.heappop(q)[1]
    print(ans)
