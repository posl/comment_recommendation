def main():
    X, Y, R = map(float, input().split())
    X = int(X * 10 ** 4)
    Y = int(Y * 10 ** 4)
    R = int(R * 10 ** 4)
    ans = 0
    for x in range(X - R, X + R + 1):
        if x % 10 ** 4 == 0:
            y = int((R ** 2 - (x - X) ** 2) ** 0.5 + Y)
            ans += y // 10 ** 4 - (Y - R) // 10 ** 4 + 1
    print(ans)
