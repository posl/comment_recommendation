def main():
    # 1. 输入数据
    a, b, c = map(int, input().split())
    # 2. 处理数据
    if a**2 + b**2 < c**2:
        print('Yes')
    else:
        print('No')
