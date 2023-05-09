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

if __name__ == '__main__':
    main()