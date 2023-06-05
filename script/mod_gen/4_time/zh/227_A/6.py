def main():
    # 读取输入
    inputs = input().split()
    N = int(inputs[0])
    K = int(inputs[1])
    A = int(inputs[2])
    # 循环K次，每次发牌
    for i in range(K):
        if A < N:
            A += 1
        else:
            A = 1
    # 输出结果
    print(A)

if __name__ == '__main__':
    main()