def main():
    # 读取输入
    A,B = map(int, input().split())
    # 计算
    print(A*B - (A+B) + 1)
