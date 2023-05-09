def main():
    n, m = map(int, input().split())
    s = []
    c = []
    for i in range(m):
        a, b = map(int, input().split())
        s.append(a)
        c.append(b)
    if n == 1:
        if m == 0:
            print(0)
        else:
            if c[0] == 0:
                print(-1)
            else:
                print(c[0])
    elif n == 2:
        if m == 0:
            print(10, 11, sep=" ")
        elif m == 1:
            if s[0] == 1:
                if c[0] == 0:
                    print(10, 11, sep=" ")
                else:
                    print(c[0]*10, c[0]*10+1, sep=" ")
            else:
                if c[0] == 0:
                    print(-1)
                else:
                    print(c[0], c[0]+10, sep=" ")
        else:
            if s[0] == 1:
                if c[0] == 0:
                    print(-1)
                else:
                    if s[1] == 2:
                        if c[1] == 0:
                            print(-1)
                        else:
                            print(c[0]*10+c[1])
                    else:
                        print(-1)
            else:
                if c[0] == 0:
                    print(-1)
                else:
                    if s[1] == 2:
                        if c[1] == 0:
                            print(-1)
                        else:
                            print(c[0]+c[1]*10)
                    else:
                        print(-1)
    elif n == 3:
        if m == 0:
            print(100, 101, 102, 103, 104, 105, 106, 107, 108, 109, sep=" ")
        elif m == 1:
            if s[0] == 1:
                if c[0] == 0:
                    print(-1)
                else:
                    print(c[0]*100, c[0]*100+1, c[0]*100+2, c[0]*100+3, c[0]*100+4, c[0]*100+5, c[0

if __name__ == '__main__':
    main()