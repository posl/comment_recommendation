def main():
    # 读取输入
    A, B = map(int, input().split())
    # 计算
    if (A >= 1 and A <= 20) and (B >= 1 and B <= 20):
        print(A * B)
    else:
        print(-1)
