def main():
    n,m = map(int,input().split())
    s = []
    t = []
    k = []
    for i in range(m):
        a,b,c = map(int,input().split())
        s.append(a)
        t.append(b)
        k.append(c)
    print(n,m)
    print(s)
    print(t)
    print(k)

if __name__ == '__main__':
    main()