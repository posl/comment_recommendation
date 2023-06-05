def main():
    # 输入
    A, B = map(int, input().split())
    # 判断
    if A > 8 or B > 8:
        print(":(")
    else:
        print("Yay!")
