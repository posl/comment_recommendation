def min_flip(S):
    # 从左到右，从右到左分别计算
    # 从左到右，如果当前字符和前一个字符相同，那么计数加1
    # 从右到左，如果当前字符和前一个字符相同，那么计数加1
    # 从左到右，从右到左，取最小值
    # 如果字符串长度为1，那么返回0
    if len(S) == 1:
        return 0
    count = 0
    for i in range(1,len(S)):
        if S[i] == S[i-1]:
            count += 1
    count2 = 0
    for i in range(len(S)-2,-1,-1):
        if S[i] == S[i+1]:
            count2 += 1
    return min(count,count2)
