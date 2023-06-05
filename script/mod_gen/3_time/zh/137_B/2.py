def main():
    # 读入数据
    k, x = map(int, input().split())
    # 计算结果
    result = list(range(x - k + 1, x + k))
    # 打印结果
    print(*result)

if __name__ == '__main__':
    main()