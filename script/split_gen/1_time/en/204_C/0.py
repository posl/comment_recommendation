def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    # city iからcity jに行けるかどうかの行列を作る
    # ここで、行列の要素は、iからjに行ける道の数
    # なお、iからjに行ける道がないときは、0とする
    # また、iからiに行ける道は、0とする
    # この行列を途中で更新していく
    # まず、iからjに行ける道があるとき、iからkに行けるかどうかの行列を更新する
    # すると、iからjに行ける道があるとき、iからkに行けるかどうかの行列が更新される
    # これを、kがN以下の数を取りうるまで繰り返す
    # そして、iからjに行ける道があるとき、iからkに行けるかどうかの行列の要素の和を求める
    # これが、iからjに行ける道の数になる
    # この行列の要素の和を求める
    # この行列の要素の和が、iからjに行ける道の数になる
    # この行列の要素の和を求める
    # この行列の要素の和が、iからjに行ける道の数になる
    # この行列の要素の
