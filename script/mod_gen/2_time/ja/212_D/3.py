def main():
    import sys
    import heapq
    input = sys.stdin.readline
    Q = int(input())
    q = []
    for _ in range(Q):
        p, *x = map(int, input().split())
        if p == 1:
            heapq.heappush(q, x[0])
        elif p == 2:
            for i in range(len(q)):
                q[i] += x[0]
        else:
            print(heapq.heappop(q))

if __name__ == '__main__':
    main()