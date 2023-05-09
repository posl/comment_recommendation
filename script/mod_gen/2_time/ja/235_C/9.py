def main():
    from bisect import bisect_left
    #入力
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0] * Q
    K = [0] * Q
    for i in range(Q):
        X[i], K[i] = map(int, input().split())
    #クエリの処理
    #Aの中でX[i]が登場するインデックスを求める
    #X[i]が複数回登場する場合は、K[i]番目のインデックスを求める
    #X[i]がK[i]番目に登場するインデックスを求める
    #X[i]がK[i]番目に登場するインデックスがNより大きい場合は-1を出力する
    #X[i]がK[i]番目に登場するインデックスがNより小さい場合は、そのインデックスを出力する
    #X[i]がK[i]番目に登場しない場合は-1を出力する
    #Aの中でX[i]が登場するインデックスを求める
    X_index = [[] for _ in range(N)]
    for i in range(N):
        X_index[i].append(i)
    #X_index[i]にはAの中でX[i]が登場するインデックスが入っている
    #X[i]がK[i]番目に登場するインデックスを求める
    for i in range(Q):
        if len(X_index[i]) >= K[i]:
            print(X_index[i][K[i] - 1] + 1)
        else:
            print(-1)

if __name__ == '__main__':
    main()