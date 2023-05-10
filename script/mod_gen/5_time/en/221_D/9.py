def main():
    """ main function
    """
    import sys
    from collections import defaultdict
    from itertools import accumulate
    input = sys.stdin.readline
    n = int(input().rstrip())
    a_b = [list(map(int, input().rstrip().split())) for _ in range(n)]
    a_b.sort()
    a = [x[0] for x in a_b]
    b = [x[1] for x in a_b]
    d = defaultdict(int)
    for i in range(n):
        d[a[i]] += 1
        d[a[i]+b[i]] -= 1
    d = sorted(d.items(), key=lambda x:x[0])
    d = list(accumulate([x[1] for x in d]))
    print(*d)

if __name__ == '__main__':
    main()