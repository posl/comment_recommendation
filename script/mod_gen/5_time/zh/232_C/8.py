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
    if n == 1:
        print("Yes")
    else:
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                else:
                    if (i+1 in a) == (j+1 in c) and (i+1 in b) == (j+1 in d):
                        continue
                    else:
                        print("No")
                        return
        print("Yes")

if __name__ == '__main__':
    main()