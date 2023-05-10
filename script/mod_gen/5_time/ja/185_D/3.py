def main():
    n,m = map(int,input().split())
    if m == 0:
        print(1)
        return
    a = list(map(int,input().split()))
    a.sort()
    a.append(n+1)
    l = []
    s = a[0]-1
    for i in range(1,m+1):
        if a[i]-a[i-1]-1 > 0:
            l.append(a[i]-a[i-1]-1)
    if len(l) == 0:
        print(0)
        return
    k = min(l)
    ans = 0
    for i in l:
        ans += (i+k-1)//k
    print(ans)

if __name__ == '__main__':
    main()