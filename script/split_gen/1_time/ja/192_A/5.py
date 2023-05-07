def main():
    #入力
    X = int(input())
    #処理
    #Xが100の倍数の場合は0を出力
    if X % 100 == 0:
        print(0)
    #Xが100の倍数でない場合は100で割った余りを出力
    else:
        print(100 - X % 100)
