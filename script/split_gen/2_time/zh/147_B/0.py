def main():
    # 输入数据
    a, b, c = map(int, input().split())
    # 判断是否bust
    if a + b + c >= 22:
        print("bust")
    else:
        print("win")
