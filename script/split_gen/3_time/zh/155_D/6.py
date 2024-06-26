def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    left = -10**18
    right = 10**18
    while right - left > 1:
        mid = (left + right) // 2
        cnt = 0
        for i in range(n):
            if a[i] >= 0:
                l = -1
                r = n
                while r - l > 1:
                    m = (l + r) // 2
                    if a[i] * a[m] <= mid:
                        r = m
                    else:
                        l = m
                cnt += n - r
            else:
                l = -1
                r = n
                while r - l > 1:
                    m = (l + r) // 2
                    if a[i] * a[m] <= mid:
                        l = m
                    else:
                        r = m
                cnt += r
            if a[i] * a[i] <= mid:
                cnt -= 1
        cnt //= 2
        if cnt < k:
            left = mid
        else:
            right = mid
    print(right)
