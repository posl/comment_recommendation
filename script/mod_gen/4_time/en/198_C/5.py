def solve():
    #import sys
    #input = sys.stdin.readline
    R, X, Y = map(int, input().split())
    import math
    d = math.sqrt(X*X + Y*Y)
    if d < R:
        return 2
    else:
        return math.ceil(d/R)
print(solve())

if __name__ == '__main__':
    solve()