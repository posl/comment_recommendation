def main():
    # 读取输入
    N, A, B = map(int, input().split())
    # 计算结果
    result = min(N * A, B)
    # 打印结果
    print(result)

if __name__ == '__main__':
    main()