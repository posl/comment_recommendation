Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    X, Y = map(int, input().split())
    for i in range(X+1):
        if 2*i + 4*(X-i) == Y:
            print('Yes')
            return
    print('No')

=======
Suggestion 2

def main():
    X, Y = map(int, input().split())
    for i in range(X+1):
        if 2*i+(X-i)*4 == Y:
            print("Yes")
            break
    else:
        print("No")

=======
Suggestion 3

def main():
    # 入力
    X, Y = map(int, input().split())

    # 処理
    for i in range(X+1):
        if 2*i + 4*(X-i) == Y:
            # 出力
            print('Yes')
            return
    # 出力
    print('No')

=======
Suggestion 4

def main():
    X, Y = map(int, input().split())
    if Y % 2 == 0 and Y // 2 >= X and 4 * X >= Y:
        print('Yes')
    else:
        print('No')
main()

=======
Suggestion 5

def main():
    X, Y = map(int, input().split())
    if X * 4 < Y or Y % 2 == 1:
        print("No")
    else:
        print("Yes")

=======
Suggestion 6

def main():
    X, Y = map(int, input().split())
    if X * 4 < Y or Y % 2 != 0:
        print("No")
    else:
        if X * 2 <= Y:
            print("Yes")
        else:
            print("No")

=======
Suggestion 7

def main():
    x,y = map(int,input().split())
    if x*4>=y and y%2==0 and x*2<=y:
        print("Yes")
    else:
        print("No")
main()

=======
Suggestion 8

def main():
    x, y = map(int, input().split())
    if x >= 0 and x <= 100 and y >= 0 and y <= 100:
        if x * 4 >= y and x * 2 <= y:
            print("Yes")
        else:
            print("No")
    else:
        print("入力値が範囲外です")

=======
Suggestion 9

def main():
    #入力
    X,Y = map(int,input().split())

    #出力
    if 2*X <= Y <= 4*X and Y%2 == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def main():
    # 入力
    X, Y = map(int, input().split())
    # 処理
    if 4 * X < Y or Y < 2 * X:
        print("No")
    elif Y % 2 == 0:
        print("Yes")
    else:
        print("No")
