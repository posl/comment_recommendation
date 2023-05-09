def main():
    #入力
    X,Y,Z = map(int,input().split())
    #処理
    tmp = X
    X = Z
    Z = Y
    Y = tmp
    #出力
    print(X,Y,Z)

if __name__ == '__main__':
    main()