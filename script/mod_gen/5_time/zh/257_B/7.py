def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    # print(N, K, Q, A, L)
    # 生成棋盘
    board = [0] * N
    for i in A:
        board[i - 1] = 1
    # print(board)
    # 棋子移动
    for i in L:
        if board[i - 1] == 1:
            continue
        else:
            # 棋子移动
            for j in range(i - 1, N):
                if board[j] == 0:
                    board[j] = 1
                    break
    # print(board)
    # 输出
    for i in range(K):
        for j in range(N):
            if board[j] == 1:
                print(j + 1, end=' ')
                board[j] = 0
                break

if __name__ == '__main__':
    main()