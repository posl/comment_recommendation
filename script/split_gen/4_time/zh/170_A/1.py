def main():
    # 读取输入
    x = list(map(int, input().split()))
    # 找出0所在的下标
    print(x.index(0) + 1)
