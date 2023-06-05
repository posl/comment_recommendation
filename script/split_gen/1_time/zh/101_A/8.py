def main():
    # 读取输入
    s = input()
    # 计算结果
    result = 0
    for c in s:
        if c == '+':
            result += 1
        else:
            result -= 1
    # 输出结果
    print(result)
