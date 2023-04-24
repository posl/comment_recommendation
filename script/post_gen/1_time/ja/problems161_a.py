Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())

    tmp = a
    a = b
    b = tmp

    tmp = a
    a = c
    c = tmp

    print(a, b, c)

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
    #操作
    X,Y = Y,X
    X,Z = Z,X
    #出力
    print(X,Y,Z)

=======
Suggestion 4

def main():
    #入力
    X,Y,Z = map(int,input().split())
    #処理
    tmp = X
    X = Y
    Y = tmp
    tmp = X
    X = Z
    Z = tmp
    #出力
    print(X,Y,Z)

=======
Suggestion 5

def main():
    x,y,z = map(int,input().split())
    print(z,x,y)

=======
Suggestion 6

def main():
    #入力
    X, Y, Z = map(int, input().split())
    #出力
    print(Z, X, Y)

=======
Suggestion 7

def main():
    a,b,c = map(int,input().split())
    print(c,a,b)

=======
Suggestion 8

def main():
    #入力
    X,Y,Z = map(int,input().split())
    
    #出力
    print(Z,X,Y)

main()

=======
Suggestion 9

def main():
    inp = input().split()
    a = int(inp[0])
    b = int(inp[1])
    c = int(inp[2])
    print(c,a,b)
    return
