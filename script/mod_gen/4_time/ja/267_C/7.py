def solve(n, m, a):
    a.sort()
    b = [0] * (n + 1)
    for i in range(n):
        b[i + 1] = b[i] + a[i]
    l = 0
    r = 2 * 10 ** 5 + 1
    while r - l > 1:
        x = (l + r) // 2
        cnt = 0
        for i in range(n):
            cnt += n - bisect.bisect_left(a, x - a[i])
        if cnt >= m:
            l = x
        else:
            r = x
    ans = 0
    cnt = 0
    for i in range(n):
        idx = bisect.bisect_left(a, l - a[i])
        cnt += n - idx
        ans += b[n] - b[idx] + a[i] * (n - idx)
    ans += (m - cnt) * l
    return ans
import bisect
n, m = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, m, a))
