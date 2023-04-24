Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if a >= 13:
        print(b)
    elif a >= 6:
        print(b // 2)
    else:
        print(0)

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if a >= 13:
        print(b)
    elif 6 <= a <= 12:
        print(b // 2)
    else:
        print(0)

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    if A >= 13:
        print(B)
    elif A >= 6:
        print(B // 2)
    else:
        print(0)

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    if a <= 5:
        print(0)
    elif a <= 12:
        print(b // 2)
    else:
        print(b)

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    if a < 6:
        print(0)
    elif a < 13:
        print(b // 2)
    else:
        print(b)

=======
Suggestion 6

def main():
    A, B = map(int, input().split())
    if A >= 13:
        print(B)
    elif A <= 5:
        print(0)
    else:
        print(B//2)

=======
Suggestion 7

def main():
    A,B = map(int,input().split())
    if A >= 13:
        print(B)
    elif A >= 6 and A <= 12:
        print(B // 2)
    else:
        print(0)

=======
Suggestion 8

def main():
    #入力
    A,B = map(int,input().split())
    #出力
    if A >= 13:
        print(B)
    elif 6 <= A <= 12:
        print(B//2)
    else:
        print(0)

=======
Suggestion 9

def main():
    #入力
    a,b = map(int,input().split())
    #出力
    if a >= 13:
        print(b)
    elif a >= 6 and a <= 12:
        print(b//2)
    else:
        print(0)
