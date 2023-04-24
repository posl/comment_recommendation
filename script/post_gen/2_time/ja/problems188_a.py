Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, y = map(int, input().split())
    if x < y:
        if x + 3 > y:
            print("Yes")
        else:
            print("No")
    else:
        if y + 3 > x:
            print("Yes")
        else:
            print("No")

=======
Suggestion 2

def main():
    X, Y = map(int, input().split())
    if X < Y:
        if Y - X < 3:
            print("Yes")
        else:
            print("No")
    else:
        if X - Y < 3:
            print("Yes")
        else:
            print("No")

=======
Suggestion 3

def main():
    x, y = map(int, input().split())
    if x > y:
        if x - y >= 3:
            print("Yes")
        else:
            print("No")
    else:
        if y - x >= 3:
            print("Yes")
        else:
            print("No")

=======
Suggestion 4

def main():
    X, Y = map(int, input().split())
    if X > Y:
        if X - Y < 3:
            print("Yes")
        else:
            print("No")
    else:
        if Y - X < 3:
            print("Yes")
        else:
            print("No")

main()

=======
Suggestion 5

def main():
    x, y = map(int, input().split())
    if x > y:
        if x - y >= 3:
            print('Yes')
        else:
            print('No')
    else:
        if y - x >= 3:
            print('Yes')
        else:
            print('No')

=======
Suggestion 6

def main():
    x, y = map(int, input().split())
    if x < y:
        if y - x <= 2:
            print("Yes")
        else:
            print("No")
    else:
        if x - y <= 2:
            print("Yes")
        else:
            print("No")

=======
Suggestion 7

def main():
    x, y = map(int, input().split())
    if x > y:
        x, y = y, x
    if x + 3 > y:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    x, y = map(int,input().split())
    if x > y:
        if x - y >= 3:
            print("No")
        else:
            print("Yes")
    else:
        if y - x >= 3:
            print("No")
        else:
            print("Yes")

=======
Suggestion 9

def main():
    x, y = map(int, input().split())
    if y - x < 3:
        print("No")
    else:
        print("Yes")

=======
Suggestion 10

def main():
    # 標準入力から得点を取得する
    x, y = map(int, input().split())
    # 優勢側の得点を求める
    if x < y:
        a = x
    else:
        a = y
    # 劣勢側の得点を求める
    if x < y:
        b = y
    else:
        b = x
    # 劣勢側が3点を取った場合の得点を求める
    c = b + 3
    # 優勢側の得点より劣勢側の得点が高い場合はYes
    if a < c:
        print("Yes")
    # 優勢側の得点より劣勢側の得点が高い場合はNo
    else:
        print("No")
