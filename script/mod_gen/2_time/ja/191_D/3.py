def main():
    X, Y, R = map(float, input().split())
    X, Y = int(X), int(Y)
    R = int(R)
    count = 0
    for x in range(X - R, X + R + 1):
        for y in range(Y - R, Y + R + 1):
            if (x - X) ** 2 + (y - Y) ** 2 <= R ** 2:
                count += 1
    print(count)

if __name__ == '__main__':
    main()