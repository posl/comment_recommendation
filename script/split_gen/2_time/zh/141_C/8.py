def main():
    # 读入输入
    s = input()
    # 计算奇数位置的字符是否是R、U或D
    for i in range(0, len(s), 2):
        if s[i] not in ['R', 'U', 'D']:
            print('No')
            return
    # 计算偶数位置的字符是否是L、U或D
    for i in range(1, len(s), 2):
        if s[i] not in ['L', 'U', 'D']:
            print('No')
            return
    # 输出结果
    print('Yes')
