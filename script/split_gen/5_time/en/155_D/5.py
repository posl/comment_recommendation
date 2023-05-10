def solve(n, k, a):
    a.sort()
    l = -10**18
    r = 10**18
    while l + 1 < r:
        x = (l + r) // 2
        cnt = 0
        for i in range(n):
            if a[i] < 0:
                cnt += n - bisect.bisect_left(a, x // a[i])
            elif a[i] == 0:
                if x >= 0:
                    cnt += n
            else:
                cnt += bisect.bisect_right(a, x // a[i])
            if a[i] * a[i] <= x:
                cnt -= 1
        cnt //= 2
        if cnt >= k:
            r = x
        else:
            l = x
    return r
import bisect
n, k = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, k, a))
