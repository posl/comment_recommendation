def main():
    import sys
    readline = sys.stdin.readline
    read = sys.stdin.read
    #n = int(readline())
    n, *xy = map(int, read().split())
    from collections import defaultdict
    d = defaultdict(int)
    for i in range(n):
        for j in range(i+1, n):
            x1, y1 = xy[2*i], xy[2*i+1]
            x2, y2 = xy[2*j], xy[2*j+1]
            d[(x2-x1, y2-y1)] += 1
            d[(x1-x2, y1-y2)] += 1
    print(n - max(d.values()))
