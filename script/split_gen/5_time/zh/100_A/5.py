def main():
    # 读入数据
    a, b = map(int, input().split())
    # 逐个判断
    if a <= 8 and b <= 8:
        print('Yay!')
    else:
        print(':(')
