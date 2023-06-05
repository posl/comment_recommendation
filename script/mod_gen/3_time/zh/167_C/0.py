def main():
    n,m,x = map(int,input().split())
    c = []
    a = []
    for i in range(n):
        c.append(list(map(int,input().split())))
        a.append(c[i][1:])
        c[i].remove(c[i][1:])
    print(c)
    print(a)

if __name__ == '__main__':
    main()