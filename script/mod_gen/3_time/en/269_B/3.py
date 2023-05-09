def main():
    s = []
    for i in range(10):
        s.append(list(input()))
    for i in range(10):
        for j in range(10):
            if s[i][j] == "#":
                s[i][j] = 1
            else:
                s[i][j] = 0
    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(10):
        for j in range(10):
            if s[i][j] == 1:
                a = i
                break
        if a != 0:
            break
    for i in range(10):
        for j in range(9,-1,-1):
            if s[i][j] == 1:
                b = i
                break
        if b != 0:
            break
    for i in range(10):
        for j in range(10):
            if s[j][i] == 1:
                c = i
                break
        if c != 0:
            break
    for i in range(10):
        for j in range(9,-1,-1):
            if s[j][i] == 1:
                d = i
                break
        if d != 0:
            break
    print(c+1,d+1)
    print(a+1,b+1)

if __name__ == '__main__':
    main()