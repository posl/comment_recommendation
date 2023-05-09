def main():
    X, Y, R = map(float, input().split())
    X = int(X * 10000)
    Y = int(Y * 10000)
    R = int(R * 10000)
    ans = 0
    for y in range(Y - R, Y + R + 1):
        if (R ** 2 - (y - Y) ** 2) >= 0:
            x = int((R ** 2 - (y - Y) ** 2) ** 0.5)
            ans += int((X + x) / 10000) - int((X - x - 1) / 10000)
    print(ans)
