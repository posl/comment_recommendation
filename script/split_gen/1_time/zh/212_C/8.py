def min_diff(a, b):
    a.sort()
    b.sort()
    ans = 10 ** 10
    for i in range(len(a)):
        l = 0
        r = len(b) - 1
        while l < r:
            m = (l + r) // 2
            if b[m] < a[i]:
                l = m + 1
            else:
                r = m
        ans = min(ans, abs(a[i] - b[l]))
        if l > 0:
            ans = min(ans, abs(a[i] - b[l - 1]))
    return ans
