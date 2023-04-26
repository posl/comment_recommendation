Synthesizing 9/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for i in range(Q):
        L, R, X = map(int, input().split())
        print(A[L-1:R].count(X))

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        l, r, x = map(int, input().split())
        print(a[l-1:r].count(x))

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for _ in range(Q):
        L, R, X = map(int, input().split())
        ans = 0
        for i in range(L-1, R):
            if A[i] == X:
                ans += 1
        print(ans)

=======
Suggestion 4

def main():
    #入力
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    Query = [list(map(int, input().split())) for _ in range(Q)]

    #初期化
    #Aの要素をインデックスに、Aの値を格納する
    #Aの値の最大値はNなので、N+1個の配列を用意する
    B = [[] for _ in range(N+1)]
    for i in range(N):
        B[A[i]].append(i)

    #クエリの処理
    for q in Query:
        l = q[0] - 1
        r = q[1] - 1
        x = q[2]
        #xの値がBのインデックスになっている
        #B[x]の要素は、Aのインデックスになっている
        #B[x]の要素がl以上r以下の範囲にあれば、xの値がAに入っている
        count = 0
        for i in B[x]:
            if l <= i <= r:
                count += 1
        print(count)

=======
Suggestion 5

def main():
    #入力
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    Query = [list(map(int, input().split())) for _ in range(Q)]
    #各数値の位置を格納するリスト
    L = [[] for _ in range(N+1)]
    for i in range(N):
        L[A[i]].append(i)
    #クエリごとに処理
    for i in range(Q):
        #クエリの値を取得
        L_i = Query[i][0]
        R_i = Query[i][1]
        X_i = Query[i][2]
        #二分探索で、X_iが最初に現れた位置と最後に現れた位置を求める
        #bisect.bisect_left(L[X_i], L_i)で、L[X_i]の中でL_i以上の値が最初に出てくる位置を返す
        #bisect.bisect_right(L[X_i], R_i)で、L[X_i]の中でR_iより大きい値が最初に出てくる位置を返す
        #その差が、X_iの値がL_i以上R_i以下の個数になる
        print(bisect.bisect_right(L[X_i], R_i) - bisect.bisect_left(L[X_i], L_i))

=======
Suggestion 6

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

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    lrx = [list(map(int, input().split())) for _ in range(q)]
    
    cnt = [0] * (n + 1)
    for i in a:
        cnt[i] += 1

    for i in range(q):
        l, r, x = lrx[i]
        print(cnt[x])

=======
Suggestion 8

def main():
    #数列の長さ
    N=int(input())
    #数列
    A=list(map(int,input().split()))
    #クエリの数
    Q=int(input())

    #クエリの処理
    for i in range(Q):
        #クエリの受け取り
        L,R,X=map(int,input().split())
        #数列の切り出し
        A_slice=A[L-1:R]
        #数列の切り出した部分の中でXと同じ値の個数をカウント
        count=A_slice.count(X)
        #出力
        print(count)
