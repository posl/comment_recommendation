def main():
    n,m = map(int, input().split())
    a = []
    b = []
    c = []
    d = []
    for i in range(m):
        a1,b1 = map(int, input().split())
        a.append(a1)
        b.append(b1)
    for i in range(m):
        c1,d1 = map(int, input().split())
        c.append(c1)
        d.append(d1)
    #print(a)
    #print(b)
    #print(c)
    #print(d)
    for i in range(m):
        for j in range(m):
            if a[i] == c[j] and b[i] == d[j]:
                a[i] = 0
                b[i] = 0
                c[j] = 0
                d[j] = 0
    #print(a)
    #print(b)
    #print(c)
    #print(d)
    if sum(a) == 0 and sum(b) == 0 and sum(c) == 0 and sum(d) == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()