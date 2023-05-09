def main():
    s = []
    for i in range(10):
        s.append(input())
    a = b = c = d = 0
    for i in range(10):
        for j in range(10):
            if s[i][j] == "#":
                if a == 0:
                    a = i + 1
                if c == 0:
                    c = j + 1
                if i + 1 > b:
                    b = i + 1
                if j + 1 > d:
                    d = j + 1
    print(a, b)
    print(c, d)

if __name__ == '__main__':
    main()