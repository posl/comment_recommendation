def problem185_b():
    n,m,t = map(int,input().split())
    a = []
    b = []
    for i in range(m):
        ai,bi = map(int,input().split())
        a.append(ai)
        b.append(bi)
    for i in range(m):
        if i == 0:
            if a[i] > 1:
                print('No')
                exit()
            else:
                n += (b[i] - a[i])
        else:
            if a[i] - b[i-1] > 1:
                print('No')
                exit()
            else:
                n += (b[i] - a[i])
    if n <= t:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    problem185_b()