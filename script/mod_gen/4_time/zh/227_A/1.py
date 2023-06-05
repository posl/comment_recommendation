def main():
    # 读取输入
    N, K, A = map(int, input().split())
    # 处理
    if K <= N:
        print(K)
    else:
        print(N - (K % N))

if __name__ == '__main__':
    main()