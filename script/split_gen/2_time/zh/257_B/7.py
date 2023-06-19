def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    # print(N, K, Q)
    # print(A)
    # print(L)
    # print(len(A), len(L))
    # print(A[0])
    # print(L[0])
    # 棋子初始位置
    chess = [0 for _ in range(N)]
    for i in range(K):
        chess[A[i]-1] += 1
    # print(chess)
    # 棋子移动
    for i in range(Q):
        for j in range(N):
            if chess[j] == 1 and j != N-1 and chess[j+1] == 0:
                chess[j] -= 1
                chess[j+1] += 1
                break
    # print(chess)
    # 棋子位置
    for i in range(K):
        print(chess[L[i]-1], end=" ")
    print()
