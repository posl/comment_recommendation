def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    #print(a)
    l = -10**18
    r = 10**18
    while l+1<r:
        x = (l+r)//2
        cnt = 0
        for i in range(n):
            if a[i]<0:
                l2 = -1
                r2 = n
                while l2+1<r2:
                    x2 = (l2+r2)//2
                    if a[i]*a[x2]<x:
                        r2 = x2
                    else:
                        l2 = x2
                cnt += n-r2
            else:
                l2 = -1
                r2 = n
                while l2+1<r2:
                    x2 = (l2+r2)//2
                    if a[i]*a[x2]<x:
                        l2 = x2
                    else:
                        r2 = x2
                cnt += r2
            if a[i]**2<x:
                cnt -= 1
        cnt //= 2
        if cnt<k:
            l = x
        else:
            r = x
    print(l)
