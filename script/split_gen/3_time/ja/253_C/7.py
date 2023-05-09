def main():
    import sys
    from collections import defaultdict
    from heapq import heappop, heappush
    input = sys.stdin.readline
    q = int(input())
    s = defaultdict(int)
    minheap = []
    maxheap = []
    for _ in range(q):
        query = input().rstrip().split()
        if query[0] == '1':
            x = int(query[1])
            s[x] += 1
            heappush(minheap, x)
            heappush(maxheap, -x)
        elif query[0] == '2':
            x = int(query[1])
            c = int(query[2])
            while c > 0 and s[x] > 0:
                s[x] -= 1
                c -= 1
            if s[x] == 0:
                while minheap and s[minheap[0]] == 0:
                    heappop(minheap)
                while maxheap and s[-maxheap[0]] == 0:
                    heappop(maxheap)
        else:
            while minheap and s[minheap[0]] == 0:
                heappop(minheap)
            while maxheap and s[-maxheap[0]] == 0:
                heappop(maxheap)
            print(-maxheap[0]-minheap[0])
