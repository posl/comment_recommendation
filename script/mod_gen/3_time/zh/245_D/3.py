def main():
    #输入
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    #计算
    B = [0] * (M + 1)
    for i in range(N + M + 1):
        for j in range(min(i + 1, N + 1)):
            B[i - j] += A[N - j] * C[i]
    #输出
    print(' '.join(map(str, B)))

if __name__ == '__main__':
    main()