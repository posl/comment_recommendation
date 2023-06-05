def main():
    # 读取输入
    a, b, c = map(int, input().split())
    # 判断
    if a**2 + b**2 < c**2:
        print('Yes')
    else:
        print('No')
