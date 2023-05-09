def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    #print(AB)
    i = 0
    ans = 0
    for day in range(1, M+1):
        while i < N and AB[i][0] == day:
            heapq.heappush(P, -AB[i][1])
            i += 1
        if P:
            ans -= heapq.heappop(P)
    print(ans)
