def main():
    # 读取输入
    n, m = map(int, input().split())
    # 计算答案
    ans = n * (n - 1) // 2 + m * (m - 1) // 2
    # 打印答案
    print(ans)
