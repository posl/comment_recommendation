def main():
    # 读取输入
    a_1, a_2, a_3, a_4 = map(int, input().split())
    # 计算结果
    result = 0
    if a_1 + a_2 + a_3 + a_4 >= 100:
        result += 1
    if a_1 + a_2 + a_3 + a_4 >= 200:
        result += 1
    if a_1 + a_2 + a_3 + a_4 >= 300:
        result += 1
    if a_1 + a_2 + a_3 + a_4 >= 400:
        result += 1
    # 输出结果
    print(result)
