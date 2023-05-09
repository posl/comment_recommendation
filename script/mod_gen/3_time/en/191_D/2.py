def main():
    x, y, r = map(float, input().split())
    # x, y, r = map(float, "0.2 0.8 1.1".split())
    # x, y, r = map(float, "100 100 1".split())
    # x, y, r = map(float, "42782.4720 31949.0192 99999.99".split())
    # print(x, y, r)
    # r = int(r)
    r = int(r) + 1
    # x = int(x)
    # y = int(y)
    x = int(x + 0.5)
    y = int(y + 0.5)
    print(x, y, r)
    count = 0
    for i in range(x - r, x + r + 1):
        for j in range(y - r, y + r + 1):
            if (i - x) ** 2 + (j - y) ** 2 <= r ** 2:
                count += 1
    print(count)

if __name__ == '__main__':
    main()