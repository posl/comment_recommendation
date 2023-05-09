def main():
    import sys
    from bisect import bisect_left, bisect_right
    readline = sys.stdin.readline
    N = int(readline())
    L = []
    R = []
    for _ in range(N):
        t, l, r = map(int, readline().split())
        if t == 1:
            L.append(l)
            R.append(r)
        elif t == 2:
            L.append(l)
            R.append(r - 1)
        elif t == 3:
            L.append(l + 1)
            R.append(r)
        else:
            L.append(l + 1)
            R.append(r - 1)
    L.sort()
    R.sort()
    ans = 0
    for i in range(N):
        l = bisect_left(R, L[i])
        r = bisect_right(L, R[i])
        ans += r - l
    print(ans)
main()
