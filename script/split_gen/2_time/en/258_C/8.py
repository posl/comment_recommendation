def main():
    N, Q = map(int, input().split())
    S = input()
    query = [list(map(int, input().split())) for _ in range(Q)]
    # 先頭の文字を基準にして、その文字の位置を記録しておく
    # その文字を削除したときに、その文字の位置がどこに移動するかを計算する
    # その文字の位置を計算するために、文字の出現回数を記録しておく
    # あとは、文字の出現回数を利用して、文字の位置を計算する
    # ただし、文字の出現回数は、文字の位置を計算するために利用するため、
    # 一度計算したら、その値を利用する
    # そのために、文字の出現回数を記録する辞書を用意する
    # この辞書は、文字の出現回数を記録するためのものであり、
    # あくまで文字の出現回数を記録するためのものであり、
    # 文字の位置を計算するために利用するためのものではない
    # 文字の位置を計算するために利用するためのものは、新たに用意する
    # 文字の位置を計算するために利用する辞書は、
    # 文字の出現回数を記録する辞書とは異なる辞書とする
    # 文字の位置を計算するために利用する辞書は、
    # 文字の出現回数を記録する辞書を利用して、
    # 文字の位置を計算する
    # この計算は、文字の出現回数を記録する辞書が更新されるたびに、
    # 文字の位置を
