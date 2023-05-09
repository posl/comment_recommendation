def main():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    AB.sort()
    ans = 0
    que = []
    for i in range(1, M + 1):
        while AB and AB[0][0] == i:
            a, b = AB.pop(0)
            heapq.heappush(que, -b)
        if que:
            ans -= heapq.heappop(que)
    print(ans)
