def main():
    # 输入字符串
    s = input()
    # 计算结果
    result = 0
    # 遍历字符串
    for i in range(0, len(s)):
        # 如果是+号，结果+1
        if s[i] == '+':
            result += 1
        # 如果是-号，结果-1
        else:
            result -= 1
    # 输出结果
    print(result)
