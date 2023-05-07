def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline
    Q = int(input())
    d = defaultdict(int)
    max_val = 0
    min_val = 0
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            d[query[1]] += 1
            if max_val == 0 and min_val == 0:
                max_val = query[1]
                min_val = query[1]
            else:
                max_val = max(query[1], max_val)
                min_val = min(query[1], min_val)
        elif query[0] == 2:
            if d[query[1]] <= query[2]:
                query[2] = d[query[1]]
            d[query[1]] -= query[2]
            if d[query[1]] == 0:
                del d[query[1]]
            if max_val == query[1]:
                if len(d) == 0:
                    max_val = 0
                    min_val = 0
                else:
                    max_val = max(d.keys())
            if min_val == query[1]:
                if len(d) == 0:
                    max_val = 0
                    min_val = 0
                else:
                    min_val = min(d.keys())
        else:
            print(max_val - min_val)

if __name__ == '__main__':
    main()