def main():
    n = int(input())
    a = []
    p = []
    x = []
    for i in range(n):
        a1,p1,x1 = map(int,input().split())
        a.append(a1)
        p.append(p1)
        x.append(x1)
    min = 1000000001
    for i in range(n):
        if a[i] < x[i]:
            if p[i] < min:
                min = p[i]
    if min == 1000000001:
        print(-1)
    else:
        print(min)

if __name__ == '__main__':
    main()