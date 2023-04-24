Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x, y = map(int, input().split())
    print((y - x + 9) // 10)

=======
Suggestion 2

def main():
    X, Y = map(int, input().split())
    print((Y - X + 9) // 10)

=======
Suggestion 3

def main():
    x, y = map(int, input().split())
    print(max(0, -(-y // 10) - x // 10))

=======
Suggestion 4

def main():
    X,Y = map(int,input().split())
    if Y % 10 == 0:
        if X <= Y:
            print(int((Y-X)/10))
        else:
            print(0)
    else:
        if X <= Y:
            print(int((Y-X)/10)+1)
        else:
            print(0)

=======
Suggestion 5

def main():
    x, y = map(int, input().split())
    print(((y + 9) // 10) * 10 - x)

=======
Suggestion 6

def main():
    X, Y = map(int, input().split())
    print(max(0, -(-Y//10) - X//10))

=======
Suggestion 7

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

=======
Suggestion 8

def main():
    x, y = map(int, input().split())
    print(max(0, (y+9)//10-x//10))

=======
Suggestion 9

def main():
    x,y=map(int,input().split())
    print(-(-y//10*10-x)//10)
main()
