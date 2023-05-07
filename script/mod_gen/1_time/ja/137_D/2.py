def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    import heapq
    hq = []
    ans = 0
    for i in range(M):
        while len(AB) > 0 and AB[0][0] == i+1:
            heapq.heappush(hq, -AB[0][1])
            AB.pop(0)
        if len(hq) > 0:
            ans -= heapq.heappop(hq)
    print(ans)

if __name__ == '__main__':
    main()