def main():
    #A,B,Cの中身を入力
    X,Y,Z = map(int,input().split())
    #AとBの中身を入れ替える
    X,Y = Y,X
    #AとCの中身を入れ替える
    X,Z = Z,X
    #A,B,Cの中身を出力
    print(X,Y,Z)

if __name__ == '__main__':
    main()