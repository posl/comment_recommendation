def main():
    L,Q = map(int,input().split())
    a = []
    for i in range(Q):
        c,x = map(int,input().split())
        if c == 1:
            a.append(x)
        else:
            a.append(x)
            a.sort()
            b = []
            for j in range(len(a)-1):
                b.append(a[j+1]-a[j])
            print(min(b))

if __name__ == '__main__':
    main()