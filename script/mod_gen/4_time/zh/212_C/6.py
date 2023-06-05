def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    ans = 10**9
    for i in range(n):
        l = 0
        r = m-1
        while l<r:
            mid = (l+r)//2
            if b[mid]<a[i]:
                l = mid+1
            else:
                r = mid
        if l>0:
            ans = min(ans,abs(a[i]-b[l-1]))
        ans = min(ans,abs(a[i]-b[l]))
        if l<m-1:
            ans = min(ans,abs(a[i]-b[l+1]))
    print(ans)

if __name__ == '__main__':
    main()