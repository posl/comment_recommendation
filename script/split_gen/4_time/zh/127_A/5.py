def main():
    # 读取输入
    A, B = map(int, input().split())
    # 计算结果
    if A >= 13:
        result = B
    elif A >= 6:
        result = B // 2
    else:
        result = 0
    # 输出结果
    print(result)
