def solve(a, b, s, t, x):
    # 二分查找
    ans = 0
    for xi in x:
        # 向西走
        left = 0
        right = a
        while left < right:
            mid = (left + right) // 2
            if s[mid] < xi:
                left = mid + 1
            else:
                right = mid
        # 向东走
        s1 = abs(xi - s[left])
        s2 = abs(xi - s[left - 1]) if left > 0 else 10 ** 10
        t1 = abs(xi - t[left])
        t2 = abs(xi - t[left - 1]) if left > 0 else 10 ** 10
        ans = min(s1, s2, t1, t2)
        print(ans)
    return
