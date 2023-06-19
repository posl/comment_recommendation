def main():
    # 读取输入
    s = input()
    # 初始化
    result = 0
    # 处理
    for i in range(4):
        if s[i] == '+':
            result += 1
        else:
            result -= 1
    # 输出
    print(result)

if __name__ == '__main__':
    main()