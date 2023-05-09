def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline
    q = int(input())
    s = defaultdict(int)
    min_s = 10**9
    max_s = 0
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            s[query[1]] += 1
            min_s = min(min_s, query[1])
            max_s = max(max_s, query[1])
        elif query[0] == 2:
            s[query[1]] -= min(s[query[1]], query[2])
            if s[query[1]] == 0:
                del s[query[1]]
                if query[1] == min_s:
                    min_s = min(s.keys())
                if query[1] == max_s:
                    max_s = max(s.keys())
        else:
            print(max_s-min_s)
    return

if __name__ == '__main__':
    main()