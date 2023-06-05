def main():
    n,m,q = map(int,input().split())
    a = [0] * (n+1)
    b = [0] * (n+1)
    c = [0] * (n+1)
    d = [0] * (n+1)
    for i in range(q):
        a[i],b[i],c[i],d[i] = map(int,input().split())
    print(a)
    print(b)
    print(c)
    print(d)
    return 0

if __name__ == '__main__':
    main()