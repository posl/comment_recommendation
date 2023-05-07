def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    #print(query)
    #print(A)
    #print(N)
    #print(Q)
    #print(query)
    
    #累積和を作る
    #cumsum = [[0 for _ in range(N+1)] for _ in range(N+1)]
    cumsum = [0] * (N+1)
    for i in range(N):
        cumsum[A[i]] += 1
    #print(cumsum)
    #print(cumsum[1])
    #print(cumsum[2])
    #print(cumsum[3])
    #print(cumsum[4])
    #print(cumsum[5])
    
    #累積和を作る
    #for i in range(N):
    #    for j in range(i+1, N+1):
    #        cumsum[i+1][j] = cumsum[i][j] + cumsum[i+1][j-1] - cumsum[i][j-1]
    #print(cumsum)
    #print(cumsum[1])
    #print(cumsum[2])
    #print(cumsum[3])
    #print(cumsum[4])
    #print(cumsum[5])
    
    #クエリごとに処理する
    for i in range(Q):
        L = query[i][0]
        R = query[i][1]
        X = query[i][2]
        #print(L)
        #print(R)
        #print(X)
        #print(cumsum[R][X] - cumsum[L-1][X])
        print(cumsum[X])
