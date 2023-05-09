def main():
    from collections import defaultdict
    import bisect
    import sys
    input = sys.stdin.readline
    q = int(input())
    a = []
    d = defaultdict(lambda: 0)
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            a.append(query[1])
            bisect.insort(a, query[1])
            d[query[1]] += 1
        elif query[0] == 2:
            if len(a) == 0 or query[1] < a[0]:
                print(-1)
            else:
                print(a[-query[2]])
        else:
            if len(a) == 0 or query[1] > a[-1]:
                print(-1)
            else:
                print(a[query[2]-1])

if __name__ == '__main__':
    main()