def main():
    import sys
    from collections import Counter
    from heapq import heappop, heappush
    input = sys.stdin.readline
    q = int(input())
    s = []
    a = []
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            s.append(query[1])
            heappush(a, query[1])
        elif query[0] == 2:
            c = query[2]
            count = Counter(s)
            for i in range(min(c, count[query[1]])):
                s.remove(query[1])
            while a and count[a[0]] == 0:
                heappop(a)
        else:
            print(a[0] - s[0])
