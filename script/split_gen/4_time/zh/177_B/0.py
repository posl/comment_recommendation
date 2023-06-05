def min_change(s, t):
    # s: str, t: str
    # return: int
    # 将s中的某些字符改变，使得t成为s的子串，求改变的最小字符数
    # 例如，将s中的第四个字符a改为c，就可以将s中的第二至第四个字符匹配到t
    # 由于s本身没有t作为它的子串，这个变化的数量--1--是最小的需要
    len_s = len(s)
    len_t = len(t)
    if len_s < len_t:
        return -1
    min_change_count = len_s
    for i in range(len_s - len_t + 1):
        change_count = 0
        for j in range(len_t):
            if s[i + j] != t[j]:
                change_count += 1
        if change_count < min_change_count:
            min_change_count = change_count
    return min_change_count
