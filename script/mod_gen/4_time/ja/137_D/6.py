def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    ans = 0
    i = 0
    from heapq import heappop, heappush
    h = []
    for day in range(M):
        while i < N and AB[i][0] == day + 1:
            heappush(h, -AB[i][1])
            i += 1
        if h:
            ans -= heappop(h)
    print(ans)

if __name__ == '__main__':
    main()