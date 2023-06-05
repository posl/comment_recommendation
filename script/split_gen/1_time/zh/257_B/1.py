def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    # print(N, K, Q)
    # print(A)
    # print(L)
    # print(len(L))
    # print(len(A))
    # 棋子的位置
    chess = [0 for i in range(N)]
    for i in range(K):
        chess[A[i]-1] = 1
    # print(chess)
    # 棋子移动
    for i in range(Q):
        # print(L[i])
        # print(chess)
        # print(chess[L[i]-1])
        if chess[L[i]-1] == 1:
            continue
        else:
            # print(chess)
            # print(L[i])
            # print(L[i]-1)
            # print(chess[L[i]-1])
            # print(chess[L[i]])
            if chess[L[i]] == 0:
                chess[L[i]-1] = 0
                chess[L[i]] = 1
            else:
                continue
            # print(chess)
    # print(chess)
    # 输出棋子位置
    for i in range(N):
        if chess[i] == 1:
            print(i+1, end=' ')
    print('')
