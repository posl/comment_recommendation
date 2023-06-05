def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[0])
    # print(ab)
    import heapq
    hq = []
    heapq.heapify(hq)
    ans = 0
    i = 0
    for d in range(1, m+1):
        while i < n and ab[i][0] <= d:
            heapq.heappush(hq, -ab[i][1])
            i += 1
        if hq:
            ans -= heapq.heappop(hq)
    print(ans)

if __name__ == '__main__':
    main()