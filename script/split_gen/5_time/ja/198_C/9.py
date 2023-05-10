def solve():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    R, X, Y = map(int, input().split())
    if R**2 > X**2 + Y**2:
        print(2)
    else:
        print((X**2 + Y**2)**0.5 // R + 1)
