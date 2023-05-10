def solve():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    ans = 10**10
    for i in range(n):
        l = 0
        r = m-1
        while l+1 < r:
            mid = (l+r)//2
            if b[mid] >= a[i]:
                r = mid
            else:
                l = mid
        ans = min(ans, abs(a[i]-b[l]))
        ans = min(ans, abs(a[i]-b[r]))
    print(ans)
