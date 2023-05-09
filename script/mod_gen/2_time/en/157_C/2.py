def main():
    n, m = map(int, input().split())
    s = [0] * m
    c = [0] * m
    for i in range(m):
        s[i], c[i] = map(int, input().split())
    if n == 1:
        if m == 0:
            print(0)
        elif m == 1:
            print(c[0])
        else:
            print(-1)
    elif n == 2:
        if m == 0:
            print(10, 11)
        elif m == 1:
            if s[0] == 1:
                print(c[0] * 10, c[0] * 10 + 1)
            else:
                print(c[0], c[0] + 10)
        elif m == 2:
            if s[0] == 1:
                if s[1] == 2:
                    print(c[0] * 10 + c[1])
                else:
                    print(-1)
            else:
                if s[1] == 1:
                    print(c[1] * 10 + c[0])
                else:
                    print(-1)
        else:
            print(-1)
    else:
        if m == 0:
            print(100, 101)
        elif m == 1:
            if s[0] == 1:
                print(c[0] * 100 + 10, c[0] * 100 + 11)
            elif s[0] == 2:
                print(c[0] * 10 + 10, c[0] * 10 + 11)
            else:
                print(c[0] + 100, c[0] + 101)
        elif m == 2:
            if s[0] == 1:
                if s[1] == 2:
                    print(c[0] * 100 + c[1] * 10)
                elif s[1] == 3:
                    print(c[0] * 100 + c[1])
                else:
                    print(-1)
            elif s[0] == 2:
                if s[1] == 1:
                    print(c[1] * 100 + c[0] * 10)
                elif s[1] ==

if __name__ == '__main__':
    main()