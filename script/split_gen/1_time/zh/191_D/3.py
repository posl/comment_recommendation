def solve():
    X, Y, R = map(float, input().split())
    X = int(X * 10000)
    Y = int(Y * 10000)
    R = int(R * 10000)
    ans = 0
    for x in range(X - R, X + R + 1):
        if (X - x) ** 2 > R ** 2:
            continue
        y = Y + (R ** 2 - (X - x) ** 2) ** 0.5
        while y > Y - 1:
            if x ** 2 + y ** 2 <= R ** 2:
                break
            y -= 1
        y = int(y)
        ans += y - (Y - 1)
    print(ans * 4)
