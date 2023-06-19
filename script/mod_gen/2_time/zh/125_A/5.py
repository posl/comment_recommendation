def main():
    # 读取输入
    A,B,T = map(int, input().split())
    # 计算结果
    count = 0
    for i in range(1, T+1):
        if i % A == 0:
            count += B
    # 输出结果
    print(count)

if __name__ == '__main__':
    main()