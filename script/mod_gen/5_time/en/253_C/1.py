def main():
    import sys
    from collections import Counter
    input = sys.stdin.readline
    q = int(input())
    s = Counter()
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            s[query[1]] += 1
        elif query[0] == 2:
            c = min(query[2], s[query[1]])
            s[query[1]] -= c
            if s[query[1]] == 0:
                del s[query[1]]
        else:
            print(max(s.keys()) - min(s.keys()))

if __name__ == '__main__':
    main()