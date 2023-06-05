def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    l = -10**18-1
    r = 10**18+1
    while r-l > 1:
        m = (l+r)//2
        cnt = 0
        for i in range(n):
            if a[i] < 0:
                cnt += n - bisect.bisect_left(a, m//a[i])
            elif a[i] > 0:
                cnt += bisect.bisect_right(a, m//a[i])
            else:
                if m >= 0:
                    cnt += n
        cnt //= 2
        if cnt < k:
            l = m
        else:
            r = m
    print(l)
