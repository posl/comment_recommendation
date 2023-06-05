def main():
    # 读取输入
    N = int(input())
    # 计算结果
    result = 1000 - N % 1000
    # 输出结果
    print(result)

if __name__ == '__main__':
    main()