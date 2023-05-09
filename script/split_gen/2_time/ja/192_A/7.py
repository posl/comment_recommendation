def main():
    #入力
    X = int(input())
    #処理
    #100の倍数の場合
    if X % 100 == 0:
        #出力
        print(100)
    else:
        #出力
        print(100 - (X % 100))
