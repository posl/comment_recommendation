def main():
    import sys
    from bisect import bisect_left
    from collections import deque
    q = int(sys.stdin.readline())
    a = deque()
    for _ in range(q):
        c, x, k = map(int, sys.stdin.readline().split())
        if c == 1:
            a.append(x)
        else:
            a.sort()
            if c == 2:
                ind = bisect_left(a, x)
                if ind >= len(a):
                    print(-1)
                else:
                    print(a[ind])
            else:
                ind = bisect_left(a, x)
                if ind == 0:
                    print(-1)
                else:
                    print(a[ind - 1])
