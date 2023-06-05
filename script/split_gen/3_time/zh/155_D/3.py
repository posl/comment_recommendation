def solve():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    l = -10**18-1
    r = 10**18+1
    while l+1<r:
        mid = (l+r)//2
        cnt = 0
        for i in range(n):
            if a[i]<0:
                cnt += n-i-1
                l = mid
            else:
                #二分查找
                l = -1
                r = n
                while l+1<r:
                    m = (l+r)//2
                    if a[i]*a[m]<mid:
                        l = m
                    else:
                        r = m
                cnt += n-r
        if cnt<k:
            l = mid
        else:
            r = mid
    print(l)
