def solve():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    #print(a)
    l = -10**18
    r = 10**18
    while l < r:
        mid = (l+r)//2
        #print(mid)
        cnt = 0
        for i in range(n):
            if a[i] < 0:
                l2 = -1
                r2 = n
                while l2 < r2:
                    mid2 = (l2+r2)//2
                    if a[i]*a[mid2] <= mid:
                        r2 = mid2
                    else:
                        l2 = mid2+1
                cnt += n-l2
            else:
                l2 = -1
                r2 = n
                while l2 < r2:
                    mid2 = (l2+r2)//2
                    if a[i]*a[mid2] <= mid:
                        l2 = mid2+1
                    else:
                        r2 = mid2
                cnt += l2
            if a[i]*a[i] <= mid:
                cnt -= 1
        #print(cnt)
        if cnt >= k:
            r = mid
        else:
            l = mid+1
    print(l)
solve()
