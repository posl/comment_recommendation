def problem257_b():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    # 1. 棋子位置
    chess = [0] * N
    for i in range(K):
        chess[A[i] - 1] = 1
    # 2. 棋子移动
    for i in range(Q):
        current = L[i] - 1
        while current < N - 1:
            if chess[current + 1] == 1:
                break
            else:
                chess[current] = 0
                chess[current + 1] = 1
                current += 1
    # 3. 输出结果
    for i in range(K):
        for j in range(N):
            if chess[j] == 1:
                print(j + 1, end=' ')
    print()

if __name__ == '__main__':
    problem257_b()