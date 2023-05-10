def main():
    s = [input() for _ in range(10)]
    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(10):
        if s[i][0] == '#':
            a = i + 1
            break
    for i in range(10):
        if s[i][9] == '#':
            b = i + 1
            break
    for i in range(10):
        if s[0][i] == '#':
            c = i + 1
            break
    for i in range(10):
        if s[9][i] == '#':
            d = i + 1
            break
    print(a, b)
    print(c, d)

if __name__ == '__main__':
    main()