def main():
    # 读入字符串
    s = input()
    # 遍历奇数位置的字符
    for i in range(0, len(s), 2):
        # 如果奇数位置的字符是大写的，则不难读
        if s[i].isupper():
            print('No')
            return
    # 遍历偶数位置的字符
    for i in range(1, len(s), 2):
        # 如果偶数位置的字符是小写的，则不难读
        if s[i].islower():
            print('No')
            return
    # 如果奇数位置的字符是小写的，偶数位置的字符是大写的，则难读
    print('Yes')
