def main():
    x, y, r = map(float, input().split())
    x = int(x * 10000)
    y = int(y * 10000)
    r = int(r * 10000)
    x1 = x - r
    x2 = x + r
    ans = 0
    for i in range(x1, x2 + 1):
        y1 = y - r
        y2 = y + r
        for j in range(y1, y2 + 1):
            if (x - i) ** 2 + (y - j) ** 2 <= r ** 2:
                ans += 1
    print(ans)
