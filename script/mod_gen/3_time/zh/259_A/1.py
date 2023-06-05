def main():
    # 读取输入
    N, M, X, T, D = map(int, input().split())
    # 算法部分
    height = T
    for i in range(X, M):
        height += D
    print(height)

if __name__ == '__main__':
    main()