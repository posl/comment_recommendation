def main():
    # 1行目に入力される文字列を取得
    line = input()
    # 1行目に入力された文字列をスペースで分割
    X, Y = line.split(" ")
    # 文字列を整数に変換
    X = int(X)
    Y = int(Y)
    
    # 10円切手を貼り足す枚数を求める
    answer = (Y - X) // 10
    
    # 答えを出力
    print(answer)

if __name__ == '__main__':
    main()