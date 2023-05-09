def solve():
    import sys
    R, X, Y = map(int, sys.stdin.readline().split())
    d = (X**2 + Y**2)**0.5
    if d < R:
        print(2)
    else:
        print(int(d//R + 1))

if __name__ == '__main__':
    solve()