def main():
    # 读取输入
    A, B = map(int, input().split())
    # 处理
    if A > 0 and B == 0:
        print("黄金")
    elif A == 0 and B > 0:
        print("银")
    else:
        print("合金")
