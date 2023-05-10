def main():
    import sys
    import math
    from decimal import Decimal
    input = sys.stdin.readline
    X, Y, R = map(Decimal, input().split())
    X = round(X * 10000)
    Y = round(Y * 10000)
    R = round(R * 10000)
    ans = 0
    for x in range(X - R, X + R + 1, 10000):
        if (R ** 2 - (x - X) ** 2).sqrt() % 10000 == 0:
            ans += 1
    ans *= 2
    for y in range(Y - R, Y + R + 1, 10000):
        if (R ** 2 - (y - Y) ** 2).sqrt() % 10000 == 0:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()