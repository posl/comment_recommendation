def main():
    #读取输入
    N = int(input())
    T = [0] * N
    X = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], X[i], A[i] = map(int, input().split())
    #计算
    result = 0
    for i in range(N):
        #计算从i开始的最大值
        #i开始的最大值
        tmp = A[i]
        for j in range(i+1, N):
            if T[j] - T[i] >= abs(X[j] - X[i]):
                tmp += A[j]
        if tmp > result:
            result = tmp
    print(result)
    return

if __name__ == '__main__':
    main()