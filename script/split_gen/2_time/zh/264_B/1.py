def main():
    # 读取输入
    r, c = map(int, input().split())
    # 逻辑处理
    if r % 2 == 0:
        if c % 2 == 0:
            print('白色')
        else:
            print('黑色')
    else:
        if c % 2 == 0:
            print('黑色')
        else:
            print('白色')
