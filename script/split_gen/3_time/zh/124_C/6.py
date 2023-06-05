def min_flip(s):
    # 从左到右遍历，如果遇到与前一个相同的，就要翻转
    n = len(s)
    cnt = 0
    for i in range(1, n):
        if s[i] == s[i-1]:
            cnt += 1
    return cnt
