def main():
    # 读取数据
    a1, a2, a3 = map(int, input().split())
    # 计算结果
    result = 0
    if a1 > a2:
        result += a1 - a2
        a1 = a2
    if a1 > a3:
        result += a1 - a3
        a1 = a3
    if a2 < a3:
        result += a3 - a2
        a3 = a2
    if a1 < a2:
        result += a2 - a1
        a2 = a1
    if a1 < a3:
        result += a3 - a1
        a3 = a1
    if a2 > a3:
        result += a2 - a3
        a2 = a3
    # 输出结果
    print(result)
