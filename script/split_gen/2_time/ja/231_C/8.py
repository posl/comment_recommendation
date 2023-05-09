def main():
    #入力
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))
    X = []
    for i in range(Q):
        X.append(int(input()))
    #身長の降順にソート
    A.sort(reverse=True)
    #print(A)
    #print(X)
    #出力
    for i in range(Q):
        print(binary_search(A,X[i]))
