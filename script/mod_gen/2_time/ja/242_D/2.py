def main():
    S = input()
    Q = int(input())
    t = []
    k = []
    for i in range(Q):
        t_i, k_i = map(int, input().split())
        t.append(t_i)
        k.append(k_i)
    # A, B, C のみからなる文字列 S が与えられます。
    # S^{(0)}:=S とし、i=1,2,3,... について S^{(i)} を S^{(i-1)} の各文字を A → BC, B → CA, C → AB と同時に置き換えたものと定義します。
    # 以下の Q 個のクエリに答えてください。i 個目のクエリの内容は以下の通りです。
    # S^{(t_i)} の先頭から k_i 文字目を出力せよ。
    # 制約
    # S は A, B, C のみからなる長さ 1 以上 10^5 以下の文字列
    # 1 ≦ Q ≦ 10^5
    # 0 ≦ t_i ≦ 10^{18}
    # 1 ≦ k_i ≦ min(10^{18}, S^{(t_i)} の長さ)
    # Q, t_i, k_i は整数
    # 文字列の長さを取得
    N = len(S)
    # 文字列の長さの最大値を取得
    N_max = 10 ** 5
    # t_i の最大値を取得
    t_max = 10 ** 18
    # 文字列の長さの最大値を取得
    N_min = 1
    # t_i の最小値を取得
    t_min = 0
    # k_i の最大値を取得
    k_max = min(10 ** 18, N)
    # k_i の最小値を取得
    k_min = 1
    # 文字列の長さを取得
    if not (

if __name__ == '__main__':
    main()