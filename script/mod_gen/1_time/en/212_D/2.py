def main():
    import heapq
    import sys
    input = sys.stdin.readline
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    ans = []
    heap = []
    for q in query:
        if q[0] == 1:
            heapq.heappush(heap, q[1])
        elif q[0] == 2:
            heap = [x + q[1] for x in heap]
            heapq.heapify(heap)
        else:
            ans.append(heapq.heappop(heap))
    print(*ans, sep='
')
main()

if __name__ == '__main__':
    main()