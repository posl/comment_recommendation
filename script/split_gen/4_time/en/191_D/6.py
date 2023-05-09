def main():
    from decimal import Decimal
    import math
    x, y, r = map(Decimal, input().split())
    x = int(x * 10000)
    y = int(y * 10000)
    r = int(r * 10000)
    ans = 0
    for i in range(x - r, x + r + 1):
        if i < 0:
            continue
        if i > 100000 * 10000:
            break
        y2 = r * r - (x - i) * (x - i)
        if y2 < 0:
            continue
        y2 = int(math.sqrt(y2))
        if y2 < 0:
            continue
        y1 = y - y2
        y2 = y + y2
        y1 = (y1 + 9999) // 10000
        y2 = y2 // 10000
        ans += y2 - y1 + 1
    print(ans)
