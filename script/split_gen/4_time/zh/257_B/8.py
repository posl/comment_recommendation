def main():
    N, K, Q = map(int, input().split())
    A = [int(x) for x in input().split()]
    L = [int(x) for x in input().split()]
    #print(N, K, Q)
    #print(A)
    #print(L)
    #棋子的位置
    chess = [0] * K
    for i in range(K):
        chess[i] = A[i]
    #print(chess)
    #操作
    for i in range(Q):
        #print("第%d次操作" % (i+1))
        #print("棋子位置：", chess)
        #print("操作：", L[i])
        #print("棋子位置：", chess)
        #print("操作：", L[i])
        #如果左边的第L_i个棋子在其最右边的方格上，则不做任何操作。
        if chess[L[i]-1] == N:
            continue
        #否则，如果右边的下一个方格上没有棋子，则将左边的第L_i个棋子向右移动一个方格；
        #如果有，则不做任何操作。
        else:
            if chess[L[i]-1] + 1 in chess:
                continue
            else:
                chess[L[i]-1] += 1
    #print("棋子位置：", chess)
    #print("操作：", L[i])
    #print("棋子位置：", chess)
    #print("操作：", L[i])
    #print("棋子位置：", chess)
    #print("操作：", L[i])
    #打印
    for i in range(K):
        print(chess[i], end=" ")
    print()
