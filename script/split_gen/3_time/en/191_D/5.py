def main():
    X, Y, R = map(float, input().split())
    X = int(X * 1000)
    Y = int(Y * 1000)
    R = int(R * 1000)
    X2 = X * X
    Y2 = Y * Y
    R2 = R * R
    x0 = X - R
    x1 = X + R
    y0 = Y - R
    y1 = Y + R
    x0 = x0 // 1000
    x1 = x1 // 1000
    y0 = y0 // 1000
    y1 = y1 // 1000
    ans = 0
    for x in range(x0, x1+1):
        for y in range(y0, y1+1):
            x2 = x * x
            y2 = y * y
            if (x2 + y2 + X2 + Y2 - 2 * x * X - 2 * y * Y) <= R2:
                ans += 1
    print(ans)
