Synthesizing 10/10 solutions (Duplicates hidden)

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
    a = list(map(int,input().split()))
    q = int(input())
    for i in range(q):
        l,r,x = map(int,input().split())
        print(a[l-1:r].count(x))

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for _ in range(Q):
        L, R, X = map(int, input().split())
        print(R - L - A[L - 1:R].count(X) + 1)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    AC = [[0]*(N+1) for _ in range(N+1)]
    for i in range(N):
        AC[i+1][A[i]] = 1
    for i in range(N):
        for j in range(1,N+1):
            AC[i+1][j] += AC[i][j]
    for _ in range(Q):
        L,R,X = map(int,input().split())
        print(AC[R][X]-AC[L-1][X])

=======
Suggestion 6

def main():
    #入力
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    LRX = [list(map(int,input().split())) for i in range(Q)]
    #Aの値をインデックスとして、その値が何番目に現れたかを記録
    #例えば、Aの値が3のものが3番目に現れたとき、A[3] = [3,3]
    #Aの値が3のものが5番目に現れたとき、A[3] = [3,5]
    #Aの値が1のものが1番目に現れたとき、A[1] = [1,1]
    #Aの値が1のものが4番目に現れたとき、A[1] = [1,4]
    #Aの値が4のものが2番目に現れたとき、A[4] = [4,2]
    #Aの値が4のものが6番目に現れたとき、A[4] = [4,6]
    #Aの値が5のものが7番目に現れたとき、A[5] = [5,7]
    #Aの値が5のものが8番目に現れたとき、A[5] = [5,8]
    for i in range(1,N+1):
        A[i-1] = [A[i-1],i]
    #Aを値でソート
    #A = [[1,1],[1,4],[3,3],[4,2],[4,6],[5,7],[5,8]]
    A.sort()
    #Aの値が同じものをまとめる
    #A = [[1,1],[1,4],[3,3],[4,2],[4,6],[5,7],[5,8]]
    #A = [[1,1,4],[3,3],[4,2,6],[5,7,8]]
    #

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    query = [list(map(int, input().split())) for _ in range(q)]
    # aの要素の個数を数える
    cnt = [0] * (n + 1)
    for i in range(n):
        cnt[a[i]] += 1
    # 累積和
    sum_cnt = [0] * (n + 1)
    for i in range(1, n + 1):
        sum_cnt[i] = sum_cnt[i - 1] + cnt[i]
    # クエリに答える
    for i in range(q):
        l, r, x = query[i]
        print(sum_cnt[r] - sum_cnt[l - 1])

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    #print(N,A,Q)
    #print("-----")
    for i in range(Q):
        L,R,X = map(int, input().split())
        #print(L,R,X)
        print(A[L-1:R].count(X))
