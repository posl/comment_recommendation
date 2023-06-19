def main():
    # 读取输入
    N, K = map(int, input().split())
    # 一次操作后的值
    N = N % K
    # 取两者的最小值
    print(min(N, abs(N-K)))

if __name__ == '__main__':
    main()