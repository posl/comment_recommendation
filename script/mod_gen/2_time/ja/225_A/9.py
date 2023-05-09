def main():
    s = input()
    # setに変換して重複を削除
    s = set(s)
    # setをリストに変換して長さを出力
    print(len(s))

if __name__ == '__main__':
    main()