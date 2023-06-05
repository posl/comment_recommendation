def main():
    n,m = map(int,input().split())
    a = []
    b = []
    c = []
    d = []
    for i in range(m):
        a1,b1 = map(int,input().split())
        a.append(a1)
        b.append(b1)
    for i in range(m):
        c1,d1 = map(int,input().split())
        c.append(c1)
        d.append(d1)
    if a == c and b == d:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()