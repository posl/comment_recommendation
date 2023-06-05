def main():
    # 读入输入
    n, k = map(int, input().split())
    # 计算最小值
    print(min(n % k, k - n % k))
