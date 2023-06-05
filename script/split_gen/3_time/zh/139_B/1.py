def main():
    # 输入
    A, B = map(int, input().split())
    # 逻辑
    if B % A == 0:
        print(B // A)
    else:
        print(B // A + 1)
