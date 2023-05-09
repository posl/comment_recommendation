def main():
    #入力
    abc = input()
    #abcをリストに変換
    abc_list = list(abc)
    #abcをリストに変換
    bca_list = abc_list[1:] + abc_list[:1]
    #abcをリストに変換
    cab_list = abc_list[2:] + abc_list[:2]
    #リストを文字列に変換
    bca = ''.join(bca_list)
    #リストを文字列に変換
    cab = ''.join(cab_list)
    #出力
    print(int(abc) + int(bca) + int(cab))
