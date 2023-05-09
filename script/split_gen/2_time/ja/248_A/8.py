def main():
    #入力
    s = input()
    #文字列をリストにする
    s_list = list(s)
    #文字列の要素を数値に変換
    s_list = [int(i) for i in s_list]
    #0~9のリストを作成
    ten_list = [i for i in range(10)]
    #リストの差集合をとる
    ans = set(ten_list) - set(s_list)
    #集合をリストに変換
    ans = list(ans)
    #リストを文字列に変換
    ans = str(ans[0])
    #出力
    print(ans)
