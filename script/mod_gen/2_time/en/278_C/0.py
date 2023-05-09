def main():
    N, Q = map(int, input().split())
    T = []
    A = []
    B = []
    for i in range(Q):
        t, a, b = map(int, input().split())
        T.append(t)
        A.append(a)
        B.append(b)
    # N = 10^9なので、N^2は10^18になる
    # 10^18はint型の最大値を超えるので、メモリが足りない
    # そのため、N×Nの行列を作るのは無理
    # そこで、N×Qの行列を作って、T_i=1のときはA_i行B_i列の要素を1にする
    # T_i=2のときはA_i行B_i列の要素を0にする
    # T_i=3のときはA_i行B_i列とB_i行A_i列の要素が両方とも1のときYes、そうでないときNoを出力する
    # このようにすれば、メモリの使用量はN×Qになる
    # また、T_i=1とT_i=2のときは、A_i行B_i列とB_i行A_i列の要素を同時に変更する必要がある
    # なので、T_i=1とT_i=2は同時に処理する
    # また、T_i=1とT_i=2のときは、A_i行B_i列とB_i行A_i列の要素を同時に変更する必要がある
    # なので、T_i=1とT_i=2は同時に処理する
    # また、T_i=1とT_i=2のときは、A_i行B_i列とB_i行A_i列の要素を同時に変更する必要がある
    # なので、T_i=1とT_i=2は同時に処理する

if __name__ == '__main__':
    main()