def main():
    # 读入数据
    a, b, c = map(int, input().split())
    # 处理数据
    if c == 0:
        if a > b:
            print('Takahashi')
        else:
            print('Aoki')
    else:
        if a >= b:
            print('Takahashi')
        else:
            print('Aoki')
