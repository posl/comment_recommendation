Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    if A >= 15 and B >= 8:
        print(1)
    elif A >= 10 and B >= 3:
        print(2)
    elif A >= 3:
        print(3)
    else:
        print(4)

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    if A + B >= 15 and B >= 8:
        print(1)
    elif A + B >= 10 and B >= 3:
        print(2)
    elif A + B >= 3:
        print(3)
    else:
        print(4)

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if a + b >= 15 and b >= 8:
        print(1)
    elif a + b >= 10 and b >= 3:
        print(2)
    elif a + b >= 3:
        print(3)
    else:
        print(4)

main()

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    if 15 <= A+B:
        print(1)
    elif 10 <= A+B:
        print(2)
    elif 3 <= A+B:
        print(3)
    else:
        print(4)

=======
Suggestion 5

def main():
    A, B = map(int, input().split())
    if A + B > 100:
        return
    if A >= 15 and B >= 8:
        print(1)
    elif A >= 10 and B >= 3:
        print(2)
    elif A >= 3:
        print(3)
    else:
        print(4)

=======
Suggestion 6

def main():
    #入力
    A, B = map(int, input().split())
    #出力
    if A + B >= 15 and B >= 8:
        print(1)
    elif A + B >= 10 and B >= 3:
        print(2)
    elif A + B >= 3:
        print(3)
    else:
        print(4)

=======
Suggestion 7

def main():
    #入力
    A, B = map(int, input().split())
    #処理
    if A + B >= 15 and B >= 8:
        ans = 1
    elif A + B >= 10 and B >= 3:
        ans = 2
    elif A + B >= 3:
        ans = 3
    else:
        ans = 4
    #出力
    print(ans)

=======
Suggestion 8

def main():
    a, b = map(int, input().split())
    if a + b > 100:
        print("error")
    else:
        if a + b >= 15 and b >= 8:
            print("1")
        elif a + b >= 10 and b >= 3:
            print("2")
        elif a + b >= 3:
            print("3")
        else:
            print("4")

=======
Suggestion 9

def main():
    a, b = map(int, input().split())
    if a + b > 100:
        print("error")
    elif a + b == 100:
        print("error")
    elif a + b < 100:
        if a >= 15 and b >= 8:
            print(1)
        elif a >= 10 and b >= 3:
            print(2)
        elif a >= 3:
            print(3)
        else:
            print(4)
    else:
        print("error")
