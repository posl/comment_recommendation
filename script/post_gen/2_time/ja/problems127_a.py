Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    if A >= 13:
        print(B)
    elif A >= 6:
        print(B // 2)
    else:
        print(0)

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if a >= 13:
        print(b)
    elif a >= 6:
        print(b // 2)
    else:
        print(0)

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    if A >= 13:
        print(B)
    elif 6 <= A <= 12:
        print(B // 2)
    else:
        print(0)

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    if A <= 5:
        print(0)
    elif A <= 12:
        print(B // 2)
    else:
        print(B)

=======
Suggestion 5

def main():
    A,B = map(int,input().split())
    if A >= 13:
        print(B)
    elif A >= 6 and A <= 12:
        print(int(B/2))
    else:
        print(0)

main()

=======
Suggestion 6

def main():
    A,B = [int(x) for x in input().split()]
    if A < 6:
        print(0)
    elif 6 <= A <= 12:
        print(B//2)
    else:
        print(B)

=======
Suggestion 7

def main():
    # A,B = map(int, input().split())
    A, B = 30, 100
    if A >= 13:
        print(B)
    elif A >= 6:
        print(B//2)
    else:
        print(0)
