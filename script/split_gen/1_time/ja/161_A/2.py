def main():
    #入力
    X,Y,Z = map(int,input().split())
    #操作
    X,Y = Y,X
    X,Z = Z,X
    #出力
    print(X,Y,Z)
