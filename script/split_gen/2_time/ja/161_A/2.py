def main():
    #入力
    X,Y,Z = map(int,input().split())
    #処理
    temp = X
    X = Z
    Z = Y
    Y = temp
    #出力
    print(X,Y,Z)
