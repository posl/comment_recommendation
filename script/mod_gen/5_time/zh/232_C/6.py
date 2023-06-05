def main():
    n, m = map(int, input().split())
    a, b = [], []
    for i in range(m):
        a0, b0 = map(int, input().split())
        a.append(a0)
        b.append(b0)
    c, d = [], []
    for i in range(m):
        c0, d0 = map(int, input().split())
        c.append(c0)
        d.append(d0)
    # print(a, b)
    # print(c, d)
    # print(n, m)
    # print(n, m)
    if n == 1:
        print('Yes')
    elif n == 2:
        if m == 0:
            print('Yes')
        elif m == 1:
            if a[0] == c[0] and b[0] == d[0]:
                print('Yes')
            else:
                print('No')
        else:
            print('No')
    elif n == 3:
        if m == 0:
            print('Yes')
        elif m == 1:
            if a[0] == c[0] and b[0] == d[0]:
                print('Yes')
            else:
                print('No')
        else:
            print('No')
    elif n == 4:
        if m == 0:
            print('Yes')
        elif m == 1:
            if a[0] == c[0] and b[0] == d[0]:
                print('Yes')
            else:
                print('No')
        elif m == 2:
            if a[0] == c[0] and b[0] == d[0] and a[1] == c[1] and b[1] == d[1]:
                print('Yes')
            else:
                print('No')
        elif m == 3:
            if a[0] == c[0] and b[0] == d[0] and a[1] == c[1] and b[1] == d[1] and a[2] == c[2] and b[2] == d[2]:
                print('Yes')
            else:
                print('No')
        elif m == 4:
            if a[0] == c[0] and b[0] == d[0]

if __name__ == '__main__':
    main()