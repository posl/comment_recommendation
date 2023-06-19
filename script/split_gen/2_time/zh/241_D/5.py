def main():
    from bisect import bisect_left, bisect_right
    from collections import defaultdict
    from sys import stdin
    input = stdin.readline
    q = int(input())
    a = []
    d = defaultdict(list)
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            a.append(query[1])
            d[query[1]].append(len(a) - 1)
        elif query[0] == 2:
            if len(a) == 0:
                print(-1)
            else:
                i = bisect_right(a, query[1])
                if i == 0:
                    print(-1)
                else:
                    print(a[d[a[i - 1]][query[2] - 1]])
        else:
            if len(a) == 0:
                print(-1)
            else:
                i = bisect_left(a, query[1])
                if i == len(a):
                    print(-1)
                else:
                    print(a[d[a[i]][query[2] - 1]])
