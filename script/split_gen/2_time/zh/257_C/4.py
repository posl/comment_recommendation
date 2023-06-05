def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    #print(N, K, Q)
    #print(A)
    #print(L)
    #print()
    
    #棋子初始位置
    chess_list = [0]*N
    for i in range(K):
        chess_list[A[i]-1] = 1
    #print(chess_list)
    
    #棋子移动
    for i in range(Q):
        for j in range(L[i]-1, N-1):
            if chess_list[j] == 1 and chess_list[j+1] == 0:
                chess_list[j], chess_list[j+1] = 0, 1
    #print(chess_list)
    
    #打印棋子位置
    for i in range(K):
        for j in range(N):
            if chess_list[j] == 1:
                print(j+1, end=' ')
    print()
