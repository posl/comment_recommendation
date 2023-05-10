def main():
    n,m = map(int,input().split())
    a = []
    b = []
    for i in range(m):
        a_i,b_i = map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    for i in range(n):
        c = 0
        d = []
        for j in range(m):
            if i+1 == a[j]:
                c += 1
                d.append(b[j])
            elif i+1 == b[j]:
                c += 1
                d.append(a[j])
        d.sort()
        print(c,end=" ")
        for j in range(len(d)):
            print(d[j],end=" ")
        print()

if __name__ == '__main__':
    main()