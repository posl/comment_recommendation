def main():
    # 读取输入
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    # 棋子位置
    P = []
    for i in range(K):
        P.append(A[i])
    # 棋子移动
    for i in range(Q):
        if P[L[i] - 1] != N:
            if P[L[i] - 1] + 1 not in P:
                P[L[i] - 1] += 1
    # 输出
    for i in range(K):
        print(P[i], end=' ')

if __name__ == '__main__':
    main()