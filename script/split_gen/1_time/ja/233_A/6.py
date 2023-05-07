def main():
    #入力
    X,Y = map(int,input().split())
    #処理
    if Y % 10 == 0:
        Y = Y // 10
    else:
        Y = Y // 10 + 1
    if X % 10 == 0:
        X = X // 10
    else:
        X = X // 10 + 1
    #出力
    print(Y-X)
