Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for _ in range(Q):
        L, R, X = map(int, input().split())
        print(A[L-1:R].count(X))

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    for i in range(Q):
        L,R,X = map(int,input().split())
        print(A[L-1:R].count(X))

=======
Suggestion 3

def main():
    #入力
    N = int(input())
    A = [int(i) for i in input().split()]
    Q = int(input())
    Query = [[int(i) for i in input().split()] for j in range(Q)]
    #問題文にある条件を満たすために、N+1の配列を用意する
    #配列の各要素には、各数字の出現回数が入る
    #例えば、Aが[3,1,4,1,5]のとき、
    #A[0]=3,A[1]=1,A[2]=4,A[3]=1,A[4]=5
    #なので、A[0]=3のとき、A[3]の値を+1する
    #答えは、A[1]=1のとき、A[4]の値を出力する
    #A[1]=1のとき、A[4]の値は、A[4]=5のとき、A[5]の値を出力する
    #A[1]=1のとき、A[4]の値は、A[4]=5のとき、A[5]=0の値を出力する
    #A[1]=1のとき、A[4]の値は、A[4]=5のとき、A[5]=0の値を出力する
    #A[1]=1のとき、A[4]の値は、A[4]=5のとき、A[5]=0の値を出力する
    #A[1]=1のとき、A[4]の値は、A[4]=5のとき、A[5]=0の値を出力する
    #A[1]=1のとき、A[4]の値は、A[4]=5のとき、A[5]=0の値を出力する
    #A[1]=1のとき、A[4]の値は、A[4]=5のとき、A[5]=0

=======
Suggestion 4

def solve():
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    L = []
    R = []
    X = []
    for i in range(Q):
        l,r,x = map(int,input().split())
        L.append(l)
        R.append(r)
        X.append(x)
    #print(N,A,Q,L,R,X)
    for i in range(Q):
        print(A[L[i]-1:R[i]].count(X[i]))

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    Query = [list(map(int, input().split())) for _ in range(Q)]
    #print(N)
    #print(A)
    #print(Q)
    #print(Query)

    #数列Aの要素をインデックスとするリストを作成
    #Aの要素をインデックスとして、Aの要素の値を格納する
    #Aの要素の値で、Aの要素のインデックスを格納する
    #Aの要素の値をインデックスとして、Aの要素の値を格納する
    #Aの要素の値で、Aの要素のインデックスを格納する
    #Aの要素の値をインデックスとして、Aの要素の値を格納する
    #Aの要素の値で、Aの要素のインデックスを格納する
    #Aの要素の値をインデックスとして、Aの要素の値を格納する
    #Aの要素の値で、Aの要素のインデックスを格納する
    #Aの要素の値をインデックスとして、Aの要素の値を格納する
    #Aの要素の値で、Aの要素のインデックスを格納する
    #Aの要素の値をインデックスとして、Aの要素の値を格納する
    #Aの要素の値で、Aの要素のインデックスを格納する
    #Aの要素の値をインデックスとして、Aの要素の値を格納する
    #Aの要素の値で、Aの要素のインデックスを格納する
    #Aの要素の値をインデックスとして、Aの要素の値を格

=======
Suggestion 6

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

=======
Suggestion 7

def main():
    #入力
    N = int(input())
    A = [int(x) for x in input().split()]
    Q = int(input())
    #クエリを入れるリスト
    L = []
    R = []
    X = []
    for i in range(Q):
        l,r,x = map(int,input().split())
        L.append(l)
        R.append(r)
        X.append(x)
    #各クエリに答える
    for i in range(Q):
        #A[L[i]-1]からA[R[i]-1]までのXの個数を数える
        print(A[L[i]-1:R[i]].count(X[i]))

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())

    # 2次元配列を作る
    # 0を作る
    arr = [[0 for i in range(n+1)] for j in range(n+1)]
    # 1を作る
    for i in range(n):
        arr[i+1][a[i]] = 1

    # 累積和をとる
    for i in range(1, n+1):
        for j in range(1, n+1):
            arr[i][j] += arr[i][j-1]

    # クエリの個数分ループ
    for i in range(q):
        l, r, x = map(int, input().split())
        print(arr[r][x] - arr[l-1][x])
