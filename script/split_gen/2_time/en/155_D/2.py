def main():
    n, k = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    if a[0] >= 0:
        print(a[k - 1])
    elif a[-1] <= 0:
        if k % 2 == 0:
            print(abs(a[-k]))
        else:
            print(a[-k])
    else:
        l = 0
        r = n - 1
        while r - l > 1:
            m = (l + r) // 2
            if a[m] < 0:
                l = m
            else:
                r = m
        if a[r] == 0:
            if k % 2 == 0:
                print(abs(a[-k]))
            else:
                print(a[-k])
        else:
            if k <= (l + 1) * (n - r):
                ans = 10 ** 18
                for i in range(l + 1):
                    j = k - (l + 1 - i) * (n - r)
                    if j > 0:
                        ans = min(ans, a[i] * a[-j])
                    else:
                        ans = min(ans, a[i] * a[-1])
                print(ans)
            else:
                ans = -10 ** 18
                for i in range(r, n):
                    j = k - (i - r + 1) * (l + 1)
                    if j > 0:
                        ans = max(ans, a[i] * a[j - 1])
                    else:
                        ans = max(ans, a[i] * a[0])
                print(ans)
