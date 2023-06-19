def main():
    # 读取输入
    s = input()
    # 初始化
    result = 0
    # 遍历字符串
    for i in s:
        if i == '+':
            result += 1
        else:
            result -= 1
    # 打印结果
    print(result)
