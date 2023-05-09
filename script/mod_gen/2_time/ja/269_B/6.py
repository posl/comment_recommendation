def main():
    s = [list(input()) for _ in range(10)]
    a = b = c = d = 0
    for i in range(10):
        for j in range(10):
            if s[i][j] == "#":
                if a == 0:
                    a = i + 1
                b = i + 1
                if c == 0:
                    c = j + 1
                d = j + 1
    print(a, b)
    print(c, d)

if __name__ == '__main__':
    main()