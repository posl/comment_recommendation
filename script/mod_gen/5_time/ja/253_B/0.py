def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    #print(s)
    #print(h, w)
    #print(s[1][2])
    c = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == "o":
                c += 1
    #print(c)
    if c == 1:
        print(0)
        exit()
    else:
        pass
    for i in range(h):
        for j in range(w):
            if s[i][j] == "o":
                #print(i, j)
                if i == 0:
                    pass
                else:
                    if s[i-1][j] == "o":
                        print(0)
                        exit()
                    else:
                        pass
                if j == 0:
                    pass
                else:
                    if s[i][j-1] == "o":
                        print(0)
                        exit()
                    else:
                        pass
                if i == h-1:
                    pass
                else:
                    if s[i+1][j] == "o":
                        print(0)
                        exit()
                    else:
                        pass
                if j == w-1:
                    pass
                else:
                    if s[i][j+1] == "o":
                        print(0)
                        exit()
                    else:
                        pass
    print(1)

if __name__ == '__main__':
    main()