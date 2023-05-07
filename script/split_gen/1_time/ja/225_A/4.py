def main():
    # 文字列Sを取得
    S = input()
    # 文字列Sの文字をリスト化
    S_list = list(S)
    # 文字列Sの文字をソート
    S_list.sort()
    # 文字列Sの文字をソートしたリストを文字列に変換
    S_sort = ''.join(S_list)
    # 文字列Sの文字をソートしたリストをsetに変換
    S_set = set(S_sort)
    # setの長さを出力
    print(len(S_set))
