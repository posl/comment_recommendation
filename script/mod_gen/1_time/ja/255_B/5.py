def main():
    import sys
    import math
    input = sys.stdin.readline
    from collections import defaultdict
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    X = defaultdict(int)
    Y = defaultdict(int)
    for i in range(N):
        x, y = map(int, input().split())
        X[i+1] = x
        Y[i+1] = y
    def is_ok(r):
        # 点iを中心とする半径rの円が点jを含むかどうか
        def contain(i, j):
            return ((X[i]-X[j])**2+(Y[i]-Y[j])**2) < r**2
        # 点iを中心とする半径rの円が点jを含むかどうか
        def contain2(i, j):
            return ((X[i]-X[j])**2+(Y[i]-Y[j])**2) <= r**2
        # 点iを中心とする半径rの円が点jを含むかどうか
        def contain3(i, j):
            return ((X[i]-X[j])**2+(Y[i]-Y[j])**2) < (r**2+1e-9)
        # 点iを中心とする半径rの円が点jを含むかどうか
        def contain4(i, j):
            return ((X[i]-X[j])**2+(Y[i]-Y[j])**2) <= (r**2+1e-9)
        # 点iを中心とする半径rの円が点jを含むかどうか
        def contain5(i, j):
            return ((X[i]-X[j])**2+(Y[i]-Y[j])**2) < (r**2-1e-9)
        # 点iを中心とする半径rの円が点jを含むかどうか
        def contain6(i, j):
            return ((X[i]-X[j])**2+(Y[i]-Y[j])**2) <= (r**2-1e-9)
        # 点iを中心とする半径rの円

if __name__ == '__main__':
    main()