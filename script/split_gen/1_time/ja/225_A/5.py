def main():
    # 文字列を入力
    S = input()
    # abcの順列を作成
    abc = list(itertools.permutations('abc', 3))
    # 文字列をリストに変換
    S = list(S)
    # 文字列をリストに変換
    S = list(S)
    # abcの順列のリストをループ
    for i in abc:
        # 文字列のリストとabcの順列のリストを比較
        if S == list(i):
            # 一致したら出力
            print(abc.index(i)+1)
