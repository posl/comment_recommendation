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
    A, B = map(int, input().split())
    if A + B >= 3 and A + B <= 18 and B >= 8:
        print(1)
    elif A + B >= 3 and A + B <= 18 and B >= 3:
        print(2)
    elif A + B >= 3 and A + B <= 18:
        print(3)
    else:
        print(4)

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    if a + b > 100:
        print("error")
        return
    if a >= 15 and b >= 8:
        print(1)
    elif a >= 10 and b >= 3:
        print(2)
    elif a >= 3:
        print(3)
    else:
        print(4)

=======
Suggestion 5

def main():
    A,B = map(int,input().split())
    if A + B > 100:
        print("ERROR")
    else:
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
    a, b = map(int, input().split())
    if a+b > 100:
        print("Error")
        return
    if a+b < 3:
        print("Error")
        return
    if a+b >= 15 and b >= 8:
        print(1)
    elif a+b >= 10 and b >= 3:
        print(2)
    elif a+b >= 3:
        print(3)
    else:
        print(4)

=======
Suggestion 7

def main():
    A, B = map(int, input().split())
    if A + B > 100:
        print("入力が不正です")
    else:
        if A + B >= 15 and B >= 8:
            print(1)
        elif A + B >= 10 and B >= 3:
            print(2)
        elif A + B >= 3:
            print(3)
        else:
            print(4)
