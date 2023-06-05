def main():
    # 读取输入
    s = input()
    # 用set去重
    s = set(s)
    # 判断长度是否为2
    if len(s) == 2:
        print('Yes')
    else:
        print('No')
