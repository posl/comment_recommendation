Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    """
    3 つの箱 A,B,C があります。それぞれの箱には、整数が 1 つ入っています。
    現在、箱 A,B,C に入っている整数はそれぞれ X,Y,Z です。
    これらの箱に対して以下の操作を順に行った後の、それぞれの箱に入っている整数を求めてください。
    箱 A と箱 B の中身を入れ替える
    箱 A と箱 C の中身を入れ替える
    """
    #入力
    X,Y,Z = map(int,input().split())
    #処理
    #箱 A と箱 B の中身を入れ替える
    tmp = X
    X = Y
    Y = tmp
    #箱 A と箱 C の中身を入れ替える
    tmp = X
    X = Z
    Z = tmp
    #出力
    print(X,Y,Z)

=======
Suggestion 2

def main():
    x, y, z = map(int, input().split())
    print(z, x, y)

=======
Suggestion 3

def main():
    X, Y, Z = map(int, input().split())
    print(Z, X, Y)

=======
Suggestion 4

def main():
    a, b, c = map(int, input().split())
    print(c, a, b)

=======
Suggestion 5

def main():
    a,b,c = map(int,input().split())
    a,b = b,a
    a,c = c,a
    print(a,b,c)

=======
Suggestion 6

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

=======
Suggestion 7

def main():
    #入力
    x,y,z = map(int, input().split())
    #操作
    x,y = y,x
    x,z = z,x
    #出力
    print(x,y,z)

=======
Suggestion 8

def main():
    #A,B,Cの中身を入力
    X,Y,Z = map(int,input().split())

    #AとBの中身を入れ替える
    X,Y = Y,X

    #AとCの中身を入れ替える
    X,Z = Z,X

    #A,B,Cの中身を出力
    print(X,Y,Z)
