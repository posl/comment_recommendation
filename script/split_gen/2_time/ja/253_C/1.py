def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline
    Q = int(input())
    d = defaultdict(int)
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            d[query[1]] += 1
        elif query[0] == 2:
            if d[query[1]] != 0:
                d[query[1]] -= min(query[2], d[query[1]])
        else:
            print(max(d) - min(d))
