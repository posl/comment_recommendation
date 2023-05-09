def main():
    from collections import Counter
    import sys
    input = sys.stdin.buffer.readline
    Q = int(input())
    D = Counter()
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            D[query[1]] += 1
        elif query[0] == 2:
            D[query[1]] -= min(query[2], D[query[1]])
            if D[query[1]] <= 0:
                del D[query[1]]
        else:
            print(max(D.keys()) - min(D.keys()))

if __name__ == '__main__':
    main()