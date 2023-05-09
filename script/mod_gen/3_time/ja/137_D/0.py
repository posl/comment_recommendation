def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    ans = 0
    que = []
    for i in range(M):
        while AB and AB[0][0] == i + 1:
            a, b = AB.pop(0)
            heapq.heappush(que, -b)
        if que:
            ans -= heapq.heappop(que)
    print(ans)

if __name__ == '__main__':
    main()