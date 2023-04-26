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
    A, B = map(int, input().split())
    if A >= 13:
        print(B)
    elif A >= 6:
        print(B // 2)
    else:
        print(0)

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    if A >= 13:
        print(B)
    elif A >= 6 and A <= 12:
        print(B // 2)
    else:
        print(0)

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    if a >= 13:
        print(b)
    elif a >= 6:
        print(int(b/2))
    else:
        print(0)

=======
Suggestion 5

def main():
    A,B = map(int,input().split())
    if A >= 13:
        print(B)
    elif A >= 6:
        print(int(B/2))
    else:
        print(0)

=======
Suggestion 6

def main():
    age, fee = map(int, input().split())
    if age < 6:
        print(0)
    elif age < 13:
        print(fee // 2)
    else:
        print(fee)

=======
Suggestion 7

def main():
    A, B = map(int, input().split())
    if A <= 5:
        print("0")
    elif A >= 6 and A <= 12:
        print(B // 2)
    else:
        print(B)

=======
Suggestion 8

def main():
    #input
    a, b = map(int, input().split())

    #output
    if a >= 13:
        print(b)
    elif a >= 6 and a <= 12:
        print(b//2)
    else:
        print(0)
