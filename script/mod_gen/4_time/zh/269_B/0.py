def main():
    s = []
    for i in range(10):
        s.append(input())
    for i in range(10):
        for j in range(10):
            if s[i][j] == '#':
                if i == 0:
                    a = i + 1
                else:
                    a = i
                if j == 0:
                    b = j + 1
                else:
                    b = j
                if i == 9:
                    c = i + 1
                else:
                    c = i + 2
                if j == 9:
                    d = j + 1
                else:
                    d = j + 2
    print(a, b)
    print(c, d)

if __name__ == '__main__':
    main()