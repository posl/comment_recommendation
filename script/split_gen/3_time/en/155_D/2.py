def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ng = -10 ** 18
    ok = 10 ** 18
    while ok - ng > 1:
        mid = (ok + ng) // 2
        cnt = 0
        for i in range(n):
            if a[i] < 0:
                l = 0
                r = n
                while r - l > 1:
                    c = (l + r) // 2
                    if a[i] * a[c] < mid:
                        l = c
                    else:
                        r = c
                cnt += n - r
            else:
                l = 0
                r = n
                while r - l > 1:
                    c = (l + r) // 2
                    if a[i] * a[c] < mid:
                        l = c
                    else:
                        r = c
                cnt += r
            if a[i] * a[i] < mid:
                cnt -= 1
        if cnt // 2 < k:
            ng = mid
        else:
            ok = mid
    print(ok)
main()
