def main():
    # 读取输入
    N = int(input())
    # 处理
    # 输出
    print(1000 - N % 1000 if N % 1000 != 0 else 0)

if __name__ == '__main__':
    main()