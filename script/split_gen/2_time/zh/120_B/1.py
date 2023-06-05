def main():
    # 读取输入
    a, b, c = map(int, input().split())
    # 计算结果
    result = min(b // a, c)
    # 输出结果
    print(result)
