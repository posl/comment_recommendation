def main():
    # 文字列入力
    S = input()
    # 文字列型のリストに変換
    S = list(S)
    # 文字列を出現順に並び替える
    S.sort()
    # 文字列の長さを取得
    S_len = len(S)
    # 文字列の中に含まれる c , h , o , k , u , d , a , i の数をカウントする
    c = S.count('c')
    h = S.count('h')
    o = S.count('o')
    k = S.count('k')
    u = S.count('u')
    d = S.count('d')
    a = S.count('a')
    i = S.count('i')
    # 文字列の中に含まれる c , h , o , k , u , d , a , i の数をリストに格納する
    S_count = [c, h, o, k, u, d, a, i]
    # 文字列の中に含まれる c , h , o , k , u , d , a , i の数を昇順に並び替える
    S_count.sort()
    # 文字列の中に含まれる c , h , o , k , u , d , a , i の数の最小値を取得する
    S_min = S_count[0]
    # 文字列の中に含まれる c , h , o , k , u , d , a , i の数の最小値が 0 ならば
    if S_min == 0:
        # 0 を出力する
        print(0)
    # 文字列の中に含まれる c , h , o , k , u , d , a , i の数の最小値が 0 でないならば
    else:
        # 文字列の長さが 8 の倍数でないならば
        if S_len % 8 != 0:
            # 0 を出力する
            print(0)
        # 文字列

if __name__ == '__main__':
    main()