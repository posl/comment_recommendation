def main():
    X, Y, R = map(float, input().split())
    X, Y = int(X * 10), int(Y * 10)
    R = int(R * 10)
    ans = 0
    for y in range(Y - R, Y + R + 1):
        x = int((R ** 2 - (y - Y) ** 2) ** 0.5)
        ans += (X + x) // 10 - (X - x - 1) // 10 + 1
    print(ans)

if __name__ == '__main__':
    main()