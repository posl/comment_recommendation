def main():
    N,M = map(int,input().split())
    a = []
    b = []
    c = []
    d = []
    for i in range(M):
        x,y = map(int,input().split())
        a.append(x)
        b.append(y)
    for i in range(M):
        x,y = map(int,input().split())
        c.append(x)
        d.append(y)
    for i in range(1,N+1):
        if i not in a:
            a.append(i)
            b.append(i)
        if i not in c:
            c.append(i)
            d.append(i)
    for i in range(N):
        for j in range(i+1,N):
            if a[i] == a[j] and b[i] == b[j]:
                if c[i] != c[j] or d[i] != d[j]:
                    print('No')
                    exit()
            if a[i] == b[j] and b[i] == a[j]:
                if c[i] != d[j] or d[i] != c[j]:
                    print('No')
                    exit()
    print('Yes')
    exit()

if __name__ == '__main__':
    main()