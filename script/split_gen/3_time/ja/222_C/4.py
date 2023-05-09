def main():
    #入力
    N, M = map(int, input().split())
    A = [list(input()) for _ in range(2*N)]
    #print(N, M)
    #print(A)
    
    #初期化
    rank = [0 for _ in range(2*N)]
    #print(rank)
    
    #試合処理
    for i in range(M):
        #print(i)
        #print(rank)
        #print(A)
        #print("---------------------------------------------------")
        #試合結果
        result = [0 for _ in range(2*N)]
        #print(result)
        for j in range(N):
            #print("j=", j)
            #print(A[2*j])
            #print(A[2*j+1])
            #print("rank=", rank)
            #print("result=", result)
            #print("---------------------------------------------------")
            #人1の手
            if A[2*j][i] == "G":
                if A[2*j+1][i] == "G":
                    #引き分け
                    result[2*j] = 0
                    result[2*j+1] = 0
                elif A[2*j+1][i] == "C":
                    #人1の勝ち
                    result[2*j] = 1
                    result[2*j+1] = -1
                elif A[2*j+1][i] == "P":
                    #人2の勝ち
                    result[2*j] = -1
                    result[2*j+1] = 1
            elif A[2*j][i] == "C":
                if A[2*j+1][i] == "G":
                    #人2の勝ち
                    result[2*j] = -1
                    result[2*j+1] = 1
                elif A[2*j+1][i] == "C":
                    #引き分け
                    result[2*j] = 0
                    result[2*j+1] = 0
                elif A[2*j+1][i] == "P":
                    #人1の勝ち
                    result[2*j] = 1
                    result[2*j+1] = -1
            elif
