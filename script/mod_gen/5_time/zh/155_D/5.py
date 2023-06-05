def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    l = -10**18
    r = 10**18
    while l+1<r:
        mid = (l+r)//2
        cnt = 0
        for i in range(n):
            if a[i]<0:
                cnt += n-bisect.bisect_right(a,mid//a[i])
            elif a[i]>0:
                cnt += bisect.bisect_left(a,mid//a[i])
            else:
                if mid>0:
                    cnt += n-i-1
        cnt //= 2
        if cnt<k:
            l = mid
        else:
            r = mid
    print(r)

if __name__ == '__main__':
    main()