def solve(s):
    # 2种情况
    # 1. 第一个是0，最后一个是1
    # 2. 第一个是1，最后一个是0
    # 2种情况下，分别计算0和1的个数，取最小的那个
    # 0和1的个数计算方法是：从第一个开始，如果和前一个不一样，就+1
    # 需要注意的是，第一个和最后一个是特殊情况，需要单独判断
    # 最后，如果只有一个字符，返回0
    if len(s) == 1:
        return 0
    if s[0] == '0':
        count0 = 1
        count1 = 0
    else:
        count0 = 0
        count1 = 1
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            if s[i] == '0':
                count0 += 1
            else:
                count1 += 1
    if s[0] == s[-1]:
        if s[0] == '0':
            count0 -= 1
        else:
            count1 -= 1
    return min(count0, count1)
