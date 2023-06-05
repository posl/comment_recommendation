def problem253_c():
    import sys
    from collections import defaultdict
    from heapq import heappush, heappop
    from heapq import heapify
    def solve():
        Q = int(sys.stdin.readline())
        S = defaultdict(int)
        min_heap = []
        max_heap = []
        for _ in range(Q):
            query = sys.stdin.readline().split()
            if query[0] == "1":
                x = int(query[1])
                S[x] += 1
                heappush(min_heap, x)
                heappush(max_heap, -x)
            elif query[0] == "2":
                x = int(query[1])
                c = int(query[2])
                while c > 0 and S[x] > 0:
                    S[x] -= 1
                    c -= 1
                if S[x] == 0:
                    while min_heap and S[min_heap[0]] == 0:
                        heappop(min_heap)
                    while max_heap and S[-max_heap[0]] == 0:
                        heappop(max_heap)
            else:
                while min_heap and S[min_heap[0]] == 0:
                    heappop(min_heap)
                while max_heap and S[-max_heap[0]] == 0:
                    heappop(max_heap)
                print(-max_heap[0] - min_heap[0])
    solve()

if __name__ == '__main__':
    problem253_c()