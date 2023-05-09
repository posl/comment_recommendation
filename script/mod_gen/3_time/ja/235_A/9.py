def main():
    #入力
    abc = input()
    #文字列を整数に変換
    abc = int(abc)
    #文字列の長さを取得
    length = len(str(abc))
    #文字列をリストに変換
    abc_list = list(str(abc))
    #リストの中身を整数に変換
    abc_list = list(map(int,abc_list))
    #変数の初期化
    bca_list = []
    cab_list = []
    #リストの中身を入れ替える
    for i in range(length):
        bca_list.append(abc_list[(i+1)%length])
        cab_list.append(abc_list[(i+2)%length])
    #リストを文字列に変換
    bca = ''.join(map(str,bca_list))
    cab = ''.join(map(str,cab_list))
    #文字列を整数に変換
    bca = int(bca)
    cab = int(cab)
    #出力
    print(abc+bca+cab)

if __name__ == '__main__':
    main()