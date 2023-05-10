def main():
    import sys
    import math
    input = sys.stdin.readline
    n, x, y = map(int, input().split())
    if x > y:
        print((n-1)*y)
    else:
        if n == 1:
            print(0)
        else:
            print((n-2)*x+y)
