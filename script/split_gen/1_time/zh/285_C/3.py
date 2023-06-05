def main():
    s = input()
    # 1. 确定长度
    # 2. 确定首字母
    # 3. 确定余下的字母
    # 4. 确定排列顺序
    # 5. 确定索引
    # 6. 打印
    # 1. 确定长度
    length = len(s)
    # 2. 确定首字母
    first = s[0]
    # 3. 确定余下的字母
    if length == 1:
        rest = 0
    else:
        rest = int(s[1:])
    # 4. 确定排列顺序
    # 5. 确定索引
    # 6. 打印
    print((ord(first) - 64) * (26 ** (length - 1)) + rest)
main()
