def solve():
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a.sort()
    def check(x):
        cnt = 0
        for i in range(n):
            if a[i] < 0:
                l = -1
                r = n
                while r - l > 1:
                    m = (l + r) // 2
                    if a[m] * a[i] < x:
                        r = m
                    else:
                        l = m
                cnt += n - r
            elif a[i] == 0:
                if x > 0:
                    cnt += n
            else:
                l = -1
                r = n
                while r - l > 1:
                    m = (l + r) // 2
                    if a[m] * a[i] < x:
                        l = m
                    else:
                        r = m
                cnt += r
                if a[i] * a[i] < x:
                    cnt -= 1
        cnt //= 2
        return cnt < k
    l = -10 ** 18
    r = 10 ** 18
    while r - l > 1:
        m = (l + r) // 2
        if check(m):
            l = m
        else:
            r = m
    print(r)
solve()
