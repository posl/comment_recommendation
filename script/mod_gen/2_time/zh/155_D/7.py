def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    l = -10**18-1
    r = 10**18+1
    while l+1 < r:
        m = (l+r)//2
        cnt = 0
        for i in range(n):
            if a[i] > 0:
                cnt += n - i - 1
                continue
            l2 = i + 1
            r2 = n
            while l2+1 < r2:
                m2 = (l2+r2)//2
                if a[i]*a[m2] <= m:
                    r2 = m2
                else:
                    l2 = m2
            cnt += n - r2
        if cnt < k:
            l = m
        else:
            r = m
    print(r)

if __name__ == '__main__':
    solve()