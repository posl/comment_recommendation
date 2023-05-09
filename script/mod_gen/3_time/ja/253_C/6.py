def main():
    import sys
    input = sys.stdin.readline
    from collections import Counter
    import heapq
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    cnt = Counter()
    minh = []
    maxh = []
    a = 0
    b = 0
    for q in query:
        if q[0] == 1:
            a += 1
            heapq.heappush(minh, q[1])
            heapq.heappush(maxh, -q[1])
        elif q[0] == 2:
            b += 1
            cnt[q[1]] += 1
        else:
            while minh[0] in cnt and cnt[minh[0]] > 0:
                heapq.heappop(minh)
            while -maxh[0] in cnt and cnt[-maxh[0]] > 0:
                heapq.heappop(maxh)
            print(-maxh[0] - minh[0])
            cnt[minh[0]] -= 1
            cnt[-maxh[0]] -= 1

if __name__ == '__main__':
    main()