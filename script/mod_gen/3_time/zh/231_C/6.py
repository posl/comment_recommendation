def main():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    x = []
    for i in range(q):
        x.append(int(input()))
    a.sort()
    for i in range(q):
        l = 0
        r = n-1
        while l<r:
            m = (l+r)//2
            if a[m]<x[i]:
                l = m+1
            else:
                r = m
        if a[l]<x[i]:
            print(0)
        else:
            print(n-l)

if __name__ == '__main__':
    main()