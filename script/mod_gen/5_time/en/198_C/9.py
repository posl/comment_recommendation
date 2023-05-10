def solve():
    import sys
    import math
    input = sys.stdin.readline
    R,X,Y = map(int, input().split())
    dist = math.sqrt(X*X+Y*Y)
    if dist == R:
        return 1
    elif dist < R:
        return 2
    else:
        return math.ceil(dist/R)
print(solve())

if __name__ == '__main__':
    solve()