def main():
    import sys
    from math import sqrt
    input = sys.stdin.readline
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(N)]
    X = [x for x, y in XY]
    Y = [y for x, y in XY]
    l = 0
    r = 10 ** 10
    while r - l > 10 ** -5:
        m = (l + r) / 2
        ok = False
        for i in range(N):
            for j in range(i + 1, N):
                if sqrt((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2) / 2 <= m:
                    ok = True
        if ok:
            r = m
        else:
            l = m
    print(l)

if __name__ == '__main__':
    main()