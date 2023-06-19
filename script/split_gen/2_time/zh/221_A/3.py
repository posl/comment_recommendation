def main():
    # 读取输入
    A, B = map(int, input().split())
    # 计算答案
    ans = 32 ** (A - B)
    # 打印答案
    print(ans)
