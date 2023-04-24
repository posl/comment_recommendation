Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x, y, z = map(int, input().split())
    print(z, x, y)

=======
Suggestion 2

def main():
    X, Y, Z = map(int, input().split())
    print(Z, X, Y)

=======
Suggestion 3

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

=======
Suggestion 4

def main():
    a,b,c = map(int,input().split())
    print(c,a,b)

=======
Suggestion 5

def main():
    #入力
    X,Y,Z = map(int,input().split())
    #出力
    print(Z,X,Y)

=======
Suggestion 6

def main():
    # リスト形式で入力
    x, y, z = map(int, input().split())
    # リストを入れ替え
    x, y = y, x
    x, z = z, x

    print(x, y, z)
