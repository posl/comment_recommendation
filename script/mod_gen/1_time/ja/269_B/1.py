def main():
    s = [input() for _ in range(10)]
    a = b = c = d = 0
    for i in range(10):
        for j in range(10):
            if s[i][j] == "#":
                a, b, c, d = i + 1, i + 1, j + 1, j + 1
    for i in range(10):
        for j in range(10):
            if s[i][j] == "#":
                a = min(a, i + 1)
                b = max(b, i + 1)
                c = min(c, j + 1)
                d = max(d, j + 1)
    print(a, b)
    print(c, d)

if __name__ == '__main__':
    main()