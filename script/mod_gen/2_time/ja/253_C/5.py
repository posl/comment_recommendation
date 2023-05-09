def main():
    import sys
    from collections import Counter
    from heapq import heappop, heappush
    input = sys.stdin.readline
    Q = int(input())
    q = []
    for _ in range(Q):
        q.append(list(map(int, input().split())))
    counter = Counter()
    heap = []
    for _q in q:
        if _q[0] == 1:
            counter[_q[1]] += 1
            heappush(heap, _q[1])
        elif _q[0] == 2:
            if _q[1] in counter:
                if counter[_q[1]] <= _q[2]:
                    del counter[_q[1]]
                    while heap[0] != _q[1]:
                        heappop(heap)
                    heappop(heap)
                else:
                    counter[_q[1]] -= _q[2]
        else:
            print(heap[-1] - heap[0])

if __name__ == '__main__':
    main()