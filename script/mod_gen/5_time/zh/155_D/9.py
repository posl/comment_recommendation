def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    l = -10**18
    r = 10**18
    while l + 1 < r:
        m = (l + r) // 2
        cnt = 0
        for i in range(n):
            if a[i] < 0:
                cnt += n - bisect.bisect_right(a, m // a[i])
            elif a[i] == 0:
                if m < 0:
                    cnt += n
            else:
                cnt += bisect.bisect_left(a, m // a[i])
            if a[i] * a[i] <= m:
                cnt -= 1
        if cnt < k:
            l = m
        else:
            r = m
    print(l)

if __name__ == '__main__':
    solve()