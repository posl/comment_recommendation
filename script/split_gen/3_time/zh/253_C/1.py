def main():
    import sys
    from collections import Counter
    from heapq import heapify, heappop, heappush
    def query1(x):
        if x in c:
            c[x] += 1
        else:
            c[x] = 1
            heappush(q, x)
    def query2(x, count):
        while count > 0:
            if x == q[0]:
                heappop(q)
                c[x] -= 1
                if c[x] == 0:
                    del c[x]
            else:
                c[x] -= 1
                heappush(q, x)
            count -= 1
    def query3():
        return q[-1] - q[0]
    q = []
    c = Counter()
    heapify(q)
    n = int(input())
    for _ in range(n):
        query = list(map(int, input().split()))
        if query[0] == 1:
            query1(query[1])
        elif query[0] == 2:
            query2(query[1], query[2])
        else:
            print(query3())
