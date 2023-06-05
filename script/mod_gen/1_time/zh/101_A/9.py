def main():
    # 读取输入
    s = input()
    # 初始值
    result = 0
    # 计算结果
    for i in range(4):
        if s[i] == '+':
            result += 1
        else:
            result -= 1
    # 输出结果
    print(result)

if __name__ == '__main__':
    main()