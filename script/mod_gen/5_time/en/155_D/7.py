def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    mod = 10**9 + 7
    pos = 0
    neg = 0
    for i in range(n):
        if a[i] < 0:
            neg += 1
        else:
            pos += 1
    if neg * pos >= k:
        l = -10**18
        r = 10**18
        while r - l > 1:
            x = (l + r) // 2
            cnt = 0
            for i in range(n):
                if a[i] < 0:
                    cnt += n - bisect.bisect_right(a, x // a[i])
                else:
                    cnt += bisect.bisect_left(a, x // a[i])
                if a[i] * a[i] <= x:
                    cnt -= 1
            cnt //= 2
            if cnt >= k:
                r = x
            else:
                l = x
        print(r)
    else:
        l = -10**18
        r = 10**18
        while r - l > 1:
            x = (l + r) // 2
            cnt = 0
            for i in range(n):
                if a[i] < 0:
                    cnt += bisect.bisect_left(a, x // a[i])
                else:
                    cnt += n - bisect.bisect_right(a, x // a[i])
                if a[i] * a[i] <= x:
                    cnt -= 1
            cnt //= 2
            if cnt >= k:
                r = x
            else:
                l = x
        print(r)

if __name__ == '__main__':
    main()