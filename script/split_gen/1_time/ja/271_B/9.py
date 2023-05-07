def main():
    N, Q = map(int, input().split())
    #数列の長さの配列
    L = []
    #数列の配列
    A = []
    for i in range(N):
        L.append(list(map(int, input().split())))
        A.append(L[i][1:])
    
    #クエリの配列
    S = []
    T = []
    for i in range(Q):
        S.append(list(map(int, input().split())))
        T.append(S[i][1])
    
    #Sの配列の要素をAの要素に変換
    for i in range(Q):
        print(A[S[i][0]-1][T[i]-1])
