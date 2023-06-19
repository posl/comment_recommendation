def main():
    #入力
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    K = []
    for _ in range(Q):
        x, k = map(int, input().split())
        X.append(x)
        K.append(k)
    #Xの値ごとにAのインデックスを取得
    X_index = [[] for _ in range(10**9+1)]
    for i, a in enumerate(A):
        X_index[a].append(i)
    #Xの値ごとにAのインデックスをソート
    for x in range(10**9+1):
        X_index[x].sort()
    #Xの値ごとにAのインデックスを二分探索
    for x, k in zip(X, K):
        if k > len(X_index[x]):
            print(-1)
        else:
            print(X_index[x][k-1]+1)
main()
