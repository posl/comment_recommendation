def main():
    import sys
    import math
    readline = sys.stdin.readline
    a, b = map(int, readline().rstrip().split())
    g = 1
    t = 0
    while g <= b:
        g += 1
        t += a / math.sqrt(g)
    print(t)

if __name__ == '__main__':
    main()