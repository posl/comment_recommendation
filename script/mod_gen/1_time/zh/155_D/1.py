def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a = a[::-1]
    print(a)
    l = -10**18
    r = 10**18
    while r - l > 1:
        mid = (r + l) // 2
        cnt = 0
        for i in range(n):
            if a[i] > 0:
                cnt += n - i - 1
                continue
            if a[i] == 0:
                continue
            ok = n
            ng = i
            while ok - ng > 1:
                m = (ok + ng) // 2
                if a[i] * a[m] > mid:
                    ok = m
                else:
                    ng = m
            cnt += n - ok
        if cnt >= k:
            r = mid
        else:
            l = mid
    print(r)

if __name__ == '__main__':
    main()