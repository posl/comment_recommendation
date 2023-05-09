def main():
    import sys
    input = sys.stdin.readline
    N, M = map(int, input().split())
    A = [input().rstrip() for _ in range(2*N)]
    #print(N,M)
    #print(A)
    # 1 から 2N の番号がついた 2N 人でじゃんけん大会をします。
    # 大会は M ラウンドからなり、各ラウンドは、全ての人が 1 度ずつ参加するような 1 対 1 の N 試合からなります。
    # i=0,1,...,M について、i ラウンド目の終了時点での順位を次のように決めます。
    # i ラウンド目までの勝数が多い方が上位
    # i ラウンド目までの勝数が同じときは、番号が小さい方が上位
    # また、i=1,...,M について、i ラウンド目の各試合の組み合わせを次のように決めます。
    # 各 k=1,2,...,N について、i-1 ラウンド目終了時点の順位が 2k-1 位の人と 2k 位の人が試合をする
    # 各試合では、対戦する 2 人がそれぞれ 1 度だけ手を出し、勝ち・負け・引き分けのいずれかの結果が発生します。
    # 未来予知ができる高橋君は、人 i が j ラウンド目の試合で出す手が A_{i,j} であることを知っています。
    # A_{i,j} は G, C, P のいずれかであり、それぞれグー

if __name__ == '__main__':
    main()