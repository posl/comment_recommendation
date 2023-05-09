def main():
    #入力
    abc = input()
    #abcをリストにする
    abc_list = list(abc)
    #print(abc_list)
    #abcをリストにする
    bca_list = [abc_list[1],abc_list[2],abc_list[0]]
    #print(bca_list)
    #abcをリストにする
    cab_list = [abc_list[2],abc_list[0],abc_list[1]]
    #print(cab_list)
    #リストを文字列に変換
    bca = "".join(bca_list)
    #print(bca)
    #リストを文字列に変換
    cab = "".join(cab_list)
    #print(cab)
    #出力
    print(int(abc)+int(bca)+int(cab))

if __name__ == '__main__':
    main()