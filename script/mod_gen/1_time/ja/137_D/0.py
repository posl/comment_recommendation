def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    ans = 0
    que = []
    for i in range(1, M + 1):
        while AB:
            a, b = AB.pop(0)
            if a <= i:
                heapq.heappush(que, -b)
            else:
                AB.append([a, b])
                break
        if que:
            ans -= heapq.heappop(que)
    print(ans)

if __name__ == '__main__':
    main()