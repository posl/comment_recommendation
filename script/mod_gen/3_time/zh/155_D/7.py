def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    left = -10**18
    right = 10**18
    while right - left > 1:
        mid = (left + right) // 2
        cnt = 0
        for i in range(n):
            if a[i] < 0:
                l = -1
                r = n
                while r - l > 1:
                    m = (l + r) // 2
                    if a[i] * a[m] < mid:
                        r = m
                    else:
                        l = m
                cnt += n - r
            elif a[i] == 0:
                if mid > 0:
                    cnt += n
            else:
                l = -1
                r = n
                while r - l > 1:
                    m = (l + r) // 2
                    if a[i] * a[m] < mid:
                        l = m
                    else:
                        r = m
                cnt += r
                cnt += n - r
        cnt //= 2
        if cnt < k:
            left = mid
        else:
            right = mid
    print(left)

if __name__ == '__main__':
    main()