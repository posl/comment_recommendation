def main():
    # 读取输入
    a, b = map(int, input().split())
    if a > 0 and b > 0:
        print("合金")
    elif a > 0 and b == 0:
        print("黄金")
    elif a == 0 and b > 0:
        print("银")
    else:
        print("输入错误")
