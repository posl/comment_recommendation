def main():
    import sys
    import math
    r, x, y = map(int, sys.stdin.readline().split())
    d = math.sqrt(x * x + y * y)
    if d < r:
        print(2)
    else:
        print(math.ceil(d / r))

if __name__ == '__main__':
    main()