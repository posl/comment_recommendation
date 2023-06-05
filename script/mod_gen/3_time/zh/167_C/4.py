def main():
    n,m,x = map(int,input().split())
    c = []
    a = []
    for i in range(n):
        c.append(list(map(int,input().split())))
    for i in range(n):
        a.append(c[i][1:])
    print(n,m,x)
    print(c)
    print(a)
    for i in range(n):
        for j in range(m):
            if a[i][j] < x:
                a[i][j] = 0
    print(a)
    for i in range(n):
        if sum(a[i]) == 0:
            print("-1")
            break
    else:
        print(sum(c[i][0] for i in range(n)))

if __name__ == '__main__':
    main()