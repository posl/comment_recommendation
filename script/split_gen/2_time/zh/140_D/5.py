def solve(n, k, s):
    # 从左边开始计算
    l = 0
    happy = 0
    for i in range(n):
        if s[i] == 'R':
            happy += 1
        else:
            happy -= 1
        if happy > 0:
            l = i+1
            break
    # 从右边开始计算
    r = n-1
    happy = 0
    for i in range(n-1, -1, -1):
        if s[i] == 'L':
            happy += 1
        else:
            happy -= 1
        if happy > 0:
            r = i-1
            break
    # 从左边开始计算
    happy = 0
    for i in range(l, r+1):
        if s[i] == 'R':
            happy += 1
        else:
            happy -= 1
    # 从右边开始计算
    happy = 0
    for i in range(r, l-1, -1):
        if s[i] == 'L':
            happy += 1
        else:
            happy -= 1
    return happy + min(k, r-l+1)
