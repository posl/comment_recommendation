def main():
    #入力
    s = []
    for i in range(10):
        s.append(input())
    #print(s)
    #処理
    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(10):
        for j in range(10):
            if s[i][j] == "#":
                a = i + 1
                break
        if a > 0:
            break
    for i in range(10):
        for j in range(10):
            if s[9-i][9-j] == "#":
                b = 10 - i
                break
        if b > 0:
            break
    for i in range(10):
        for j in range(10):
            if s[j][i] == "#":
                c = i + 1
                break
        if c > 0:
            break
    for i in range(10):
        for j in range(10):
            if s[9-j][9-i] == "#":
                d = 10 - i
                break
        if d > 0:
            break
    #出力
    print(a,b)
    print(c,d)
main()

if __name__ == '__main__':
    main()