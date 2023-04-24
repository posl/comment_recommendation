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

main()

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
    a, b = map(int, input().split())
    if a >= 13:
        print(b)
    elif a >= 6:
        print(b // 2)
    else:
        print(0)

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    if A >= 13:
        print(B)
    elif A >= 6:
        print(B//2)
    else:
        print(0)

=======
Suggestion 5

def main():
    A, B = map(int, input().split())
    if A >= 13:
        print(B)
    elif A <= 5:
        print(0)
    else:
        print(B // 2)

=======
Suggestion 6

def main():
    a, b = list(map(int, input().split()))
    if a >= 13:
        print(b)
    elif a >= 6:
        print(b // 2)
    else:
        print(0)
