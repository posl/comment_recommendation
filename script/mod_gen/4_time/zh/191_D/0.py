def main():
    X, Y, R = map(float, input().split())
    X = int(X * 10000)
    Y = int(Y * 10000)
    R = int(R * 10000)
    ans = 0
    for x in range(X - R, X + R + 1):
        d = R * R - (X - x) ** 2
        if d < 0:
            continue
        d = int(d ** 0.5)
        y1 = Y + d
        y2 = Y - d
        ans += (y1 // 10000 - y2 // 10000 + 1)
    print(ans)

if __name__ == '__main__':
    main()