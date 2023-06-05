def main():
    # 读取输入
    a, b = map(int, input().split())
    # 计算
    if b % a == 0:
        result = a + b
    else:
        result = b - a
    # 输出结果
    print(result)
