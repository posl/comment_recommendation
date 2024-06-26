def main():
    K = int(input())
    S = input()[:-1]
    T = input()[:-1]
    print(S)
    print(T)
    # 1, 2, ..., 9 が表に書かれたカードが K 枚ずつ、計 9K 枚のカードがある
    # これらのカードをランダムにシャッフルして、高橋くんと青木くんにそれぞれ、4 枚を表向きに、1 枚を裏向きにして配る
    # 高橋くんに配られたカードが文字列 S として、青木くんに配られたカードが文字列 T として与えられる
    # S, T は 5 文字の文字列で、先頭 4 文字は 1, 2, ..., 9 からなり、表向きのカードに書かれた数を表す
    # 末尾 1 文字は # であり、裏向きのカードであることを表す
    # 5 枚の手札の点数を、c_i をその手札に含まれる i の枚数として、 sum_{i=1}^9 i × 10^{c_i} で定義する
    # 高橋くんが青木くんより点数の高い手札を持っていたら高橋くんの勝ち
    # 高橋くんの勝つ確率を求める
    # 2 ≤ K ≤ 10^5
    # |S| = |T| = 5
    # S, T の 1 文字目から 4 文字目は 1, 2, ..., 9 のいずれか
    # 1, 2, ..., 9 はそれぞれ、S と T に合計 K 回までしか出現しない
    # S, T の 5

if __name__ == '__main__':
    main()