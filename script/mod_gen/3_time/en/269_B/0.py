def main():
    s = []
    for i in range(10):
        s.append(input())
    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(10):
        for j in range(10):
            if s[i][j] == '#':
                if a == 0:
                    a = i
                if b == 0:
                    b = i
                if c == 0:
                    c = j
                if d == 0:
                    d = j
                if i < a:
                    a = i
                if i > b:
                    b = i
                if j < c:
                    c = j
                if j > d:
                    d = j
    print(a+1, b+1)
    print(c+1, d+1)

if __name__ == '__main__':
    main()