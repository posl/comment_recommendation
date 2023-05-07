def main():
    import sys
    from bisect import bisect_left
    from collections import deque
    input = sys.stdin.readline
    L,Q = map(int,input().split())
    L = L
    Q = Q
    d = deque()
    d.append(0)
    d.append(L)
    for i in range(Q):
        c,x = map(int,input().split())
        if c == 1:
            d.append(x)
            d = deque(sorted(d))
        if c == 2:
            idx = bisect_left(d,x)
            print(d[idx]-d[idx-1])
