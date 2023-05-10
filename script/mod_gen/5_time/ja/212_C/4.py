def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    ans = 10**9
    for i in a:
        l = 0
        r = m-1
        while l <= r:
            mid = (l+r)//2
            if b[mid] < i:
                l = mid+1
            else:
                r = mid-1
        if l < m:
            ans = min(ans,abs(i-b[l]))
        if r >= 0:
            ans = min(ans,abs(i-b[r]))
    print(ans)

if __name__ == '__main__':
    main()