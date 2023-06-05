def main():
    # 读取输入
    S = input()
    # 计算结果
    result = 0
    for i in range(4):
        if S[i] == '+':
            result += 1
        else:
            result -= 1
    # 打印结果
    print(result)

if __name__ == '__main__':
    main()