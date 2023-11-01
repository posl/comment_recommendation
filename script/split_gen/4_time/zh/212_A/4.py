def main():
    # 读入数据
    a, b = map(int, input().split())
    # 输出结果
    if a == 0:
        print('Silver')
    elif b == 0:
        print('Gold')
    else:
