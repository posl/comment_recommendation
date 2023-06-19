def main():
    # 读取输入
    a = [int(x) for x in input().split()]
    # 计算
    total = sum(a)
    # 输出
    if total >= 22:
        print('bust')
    else:
        print('win')
