def main():
    # 读取输入
    a, b = map(int, input().split())
    # 计算
    if a <= 9 and b <= 9:
        print(a * b)
    else:
        print(-1)
