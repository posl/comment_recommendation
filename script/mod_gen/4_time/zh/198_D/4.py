def solve(s1,s2,s3):
    # print(s1, s2, s3)
    # 1. 长度不一样，直接返回
    if len(s1) != len(s2) or len(s1) != len(s3):
        return
    # 2. 重复字符的个数
    s = s1 + s2 + s3
    # print(s)
    d = {}
    for c in s:
        d[c] = d.get(c, 0) + 1
    # print(d)
    if len(d) > 10:
        return
    # 3. 重复字符的个数
    # print(s1, s2, s3)
    # 4. 字符对应的数字
    d = {}
    for c in s:
        d[c] = 0
    # print(d)
    # 5. 重复字符的个数
    # print(s1, s2, s3)
    # 6. 字符对应的数字
    d = {}
    for c in s:
        d[c] = 0
    # print(d)
    # 7. 重复字符的个数
    # print(s1, s2, s3)
    # 8. 字符对应的数字
    d = {}
    for c in s:
        d[c] = 0
    # print(d)
    # 9. 重复字符的个数
    # print(s1, s2, s3)
    # 10. 字符对应的数字
    d = {}
    for c in s:
        d[c] = 0
    # print(d)
    # 11. 重复字符的个数
    # print(s1, s2, s3)
    # 12. 字符对应的数字
    d = {}
    for c in s:
        d[c] = 0
    # print(d)
    # 13. 重复字符的个数
    # print(s1, s2, s3)
    # 14. 字符对应的数字
    d = {}
    for c in s:
        d[c] = 0
    # print(d)
    # 15.

if __name__ == '__main__':
    solve()