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
