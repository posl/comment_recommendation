def main():
    # 读入数据
    H, A = map(int, input().split())
    # 计算
    print((H + A - 1) // A)
