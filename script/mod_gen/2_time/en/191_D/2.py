def main():
    X, Y, R = map(float, input().split())
    X = int(X * 10000)
    Y = int(Y * 10000)
    R = int(R * 10000)
    ans = 0
    for x in range(X - R, X + R + 1):
        if x < 0 or x > 10 ** 10:
            continue
        y = int((R ** 2 - (x - X) ** 2) ** 0.5)
        ans += (Y + y) // 10000 - (Y - y) // 10000 + 1
    print(ans)

if __name__ == '__main__':
    main()