def main():
    # 读取数据
    N, M, X, T, D = map(int, input().split())
    # 求和
    sum = T
    for i in range(X, M):
        sum += D
    print(sum)

if __name__ == '__main__':
    main()