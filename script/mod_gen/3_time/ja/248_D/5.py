def main():
    #入力
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    Query = [list(map(int,input().split())) for _ in range(Q)]
    
    #処理
    #Aを値でソートした時のインデックスを求める
    B = sorted(A)
    Index = [0]*N
    for i in range(N):
        Index[B[i]-1] = i
    
    #Indexを累積和で求める
    Cumsum = [0]*(N+1)
    for i in range(N):
        Cumsum[i+1] = Cumsum[i] + Index[i]
    
    #クエリに対する処理
    for i in range(Q):
        L = Query[i][0]
        R = Query[i][1]
        X = Query[i][2]
        print(Cumsum[R]-Cumsum[L-1])

if __name__ == '__main__':
    main()