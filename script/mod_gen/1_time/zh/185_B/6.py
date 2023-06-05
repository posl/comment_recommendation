def main():
    n,m,t = map(int,input().split())
    a = []
    b = []
    for i in range(m):
        a_i,b_i = map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    for i in range(m):
        if i == 0:
            if a[i] != 1:
                print('No')
                exit()
        else:
            if a[i] != b[i-1]+1:
                print('No')
                exit()
    if b[m-1] != t:
        print('No')
        exit()
    if n == 1:
        print('No')
        exit()
    if n == 2:
        print('Yes')
        exit()
    if n == 3:
        if m == 1:
            print('No')
            exit()
        else:
            print('Yes')
            exit()
    if n == 4:
        if m == 1:
            print('No')
            exit()
        else:
            if a[0] == 1 and b[0] == 2:
                print('No')
                exit()
            else:
                print('Yes')
                exit()
    if n == 5:
        if m == 1:
            print('No')
            exit()
        else:
            if a[0] == 1 and b[0] == 2:
                print('No')
                exit()
            else:
                if a[0] == 3 and b[0] == 4:
                    print('No')
                    exit()
                else:
                    print('Yes')
                    exit()
    if n == 6:
        if m == 1:
            print('No')
            exit()
        else:
            if a[0] == 1 and b[0] == 2:
                print('No')
                exit()
            else:
                if a[0] == 3 and b[0] == 4:
                    print('No')
                    exit()
                else:
                    if a[0] == 5 and b[0] == 6:
                        print('No')
                        exit()
                    else:
                        print('Yes')
                        exit()
    if n == 7:
        if m == 1:
            print('No')
            exit()
        else:
            if a[0] == 1 and b[0]

if __name__ == '__main__':
    main()