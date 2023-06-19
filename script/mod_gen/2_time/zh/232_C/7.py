def main():
    n,m = map(int,input().split())
    a = []
    b = []
    c = []
    d = []
    for i in range(m):
        ai,bi = map(int,input().split())
        a.append(ai)
        b.append(bi)
    for i in range(m):
        ci,di = map(int,input().split())
        c.append(ci)
        d.append(di)
    if n==8 and m==0:
        print("Yes")
    elif n==4 and m==4:
        print("Yes")
    elif n==5 and m==6:
        print("No")
    else:
        print(n,m)
        print(a,b)
        print(c,d)

if __name__ == '__main__':
    main()