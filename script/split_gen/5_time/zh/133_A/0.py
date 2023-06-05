def main():
    # 读入数据
    n, a, b = map(int, input().split())
    # 计算最小值
    print(min(n*a, b))
