def main():
    from decimal import Decimal
    import math
    X, Y, R = map(Decimal, input().split())
    X = int(X * 10000)
    Y = int(Y * 10000)
    R = int(R * 10000)
    ans = 0
    for x in range(X - R, X + R + 1):
        if (R ** 2 - (X - x) ** 2).sqrt() % 10000 != 0:
            continue
        y = (R ** 2 - (X - x) ** 2).sqrt()
        ans += (Y + y) // 10000 - (Y - y) // 10000 + 1
    print(ans)
