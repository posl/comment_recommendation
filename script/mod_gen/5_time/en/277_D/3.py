def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    b = []
    for i in range(n):
        if i == 0:
            b.append(a[i])
        elif a[i] != a[i-1]:
            b.append(a[i])
    n = len(b)
    if n == 1:
        print(0)
    elif n == 2:
        if (b[1]-b[0])%m == 1:
            print(0)
        else:
            print(b[0]+b[1])
    else:
        c = []
        for i in range(n):
            if i == 0:
                c.append(b[i])
            elif b[i] != b[i-1]+1:
                c.append(b[i])
        n = len(c)
        if n == 1:
            print(0)
        elif n == 2:
            print(c[0]+c[1])
        else:
            print(sum(c))

if __name__ == '__main__':
    main()