def harvest(n, a):
    ans = 0
    for i in range(n):
        if a[i] > 10:
            ans += a[i] - 10
    return ans
