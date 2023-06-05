def kthString(a, b, k):
    if a == 0:
        return 'b' * b
    if b == 0:
        return 'a' * a
    # 以a开头的字符串的数量
    aNum = 1
    for i in range(a + b):
        if aNum >= k:
            break
        if aNum + (a + b - i - 1) >= k:
            break
        aNum = aNum * (a + b - i) // (i + 1)
    if aNum >= k:
        return 'a' + kthString(a - 1, b, k)
    else:
        return 'b' + kthString(a, b - 1, k - aNum)
