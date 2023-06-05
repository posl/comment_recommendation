def main():
    # 读取数据
    a, b = map(int, input().split())
    # 逻辑处理
    if a > 0 and b == 0:
        print('黄金')
    elif a == 0 and b > 0:
        print('银')
    else:
        print('合金')
