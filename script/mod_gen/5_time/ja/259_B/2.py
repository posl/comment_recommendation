def main():
    import sys
    import math
    a, b, d = map(int, sys.stdin.readline().split())
    rad = math.radians(d)
    x = a * math.cos(rad) - b * math.sin(rad)
    y = a * math.sin(rad) + b * math.cos(rad)
    print(x, y)
main()

if __name__ == '__main__':
    main()