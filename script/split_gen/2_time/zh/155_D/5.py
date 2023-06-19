def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    left = -10**18
    right = 10**18
    while left + 1 < right:
        mid = (left + right) // 2
        cnt = 0
        for i in range(n):
            if a[i] < 0:
                l = -1
                r = n
                while l + 1 < r:
                    m = (l + r) // 2
                    if a[m] * a[i] < mid:
                        r = m
                    else:
                        l = m
                cnt += n - r
            else:
                l = -1
                r = n
                while l + 1 < r:
                    m = (l + r) // 2
                    if a[m] * a[i] < mid:
                        l = m
                    else:
                        r = m
                cnt += r
            if a[i] * a[i] < mid:
                cnt -= 1
        cnt //= 2
        if cnt < k:
            left = mid
        else:
            right = mid
    print(left)
solve()
