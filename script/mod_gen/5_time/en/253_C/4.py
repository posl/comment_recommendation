def solve():
    from sys import stdin
    from collections import Counter
    from heapq import heappush, heappop
    input = stdin.readline
    q = int(input())
    s = Counter()
    minheap = []
    maxheap = []
    for _ in range(q):
        query = tuple(map(int, input().split()))
        if query[0] == 1:
            s[query[1]] += 1
            heappush(minheap, query[1])
            heappush(maxheap, -query[1])
        elif query[0] == 2:
            while s and query[2]:
                if s[minheap[0]] <= query[2]:
                    query[2] -= s[minheap[0]]
                    s.pop(minheap[0])
                    heappop(minheap)
                else:
                    s[minheap[0]] -= query[2]
                    query[2] = 0
        else:
            while s and s[minheap[0]] == 0:
                s.pop(minheap[0])
                heappop(minheap)
            while s and s[-maxheap[0]] == 0:
                s.pop(-maxheap[0])
                heappop(maxheap)
            print(-maxheap[0] - minheap[0])

if __name__ == '__main__':
    solve()