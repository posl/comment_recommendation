def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0] * Q
    K = [0] * Q
    for i in range(Q):
        X[i], K[i] = map(int, input().split())
    #print("A:", A)
    #print("X:", X)
    #print("K:", K)
    #Aの各要素の値が最初に出現する位置を格納するリストを作成
    #Aの要素の値は最大で10^9なので10^9+1の要素数を持つリストを作成
    #Aの要素の値が出現しない場合は-1を格納する
    A_first = [-1] * (10**9+1)
    for i in range(N):
        if A_first[A[i]] == -1:
            A_first[A[i]] = i+1
    #print(A_first)
    #Xの各要素の値が最初に出現する位置を格納するリストを作成
    #Xの要素の値は最大で10^9なので10^9+1の要素数を持つリストを作成
    #Xの要素の値が出現しない場合は-1を格納する
    X_first = [-1] * (10**9+1)
    for i in range(Q):
        if X_first[X[i]] == -1:
            X_first[X[i]] = i+1
    #print(X_first)
    #Aの各要素の値がK回目に出現する位置を格納するリストを作成
    #Aの要素の値は最大で10^9なので10^9+1の要素数を持つリストを作成
    #Aの要素の値がK回目に出現しない場合は-1を格納する
    A_K = [-1] * (10**9+1)
    for i in range(N
