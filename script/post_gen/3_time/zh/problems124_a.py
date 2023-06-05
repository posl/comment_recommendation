Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_coins(a,b):
    if a == b:
        return a*2
    elif a > b:
        return (a-1)*2
    else:
        return (b-1)*2

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if a > b:
        print(a + (a - 1))
    elif a < b:
        print(b + (b - 1))
    else:
        print(a + b)

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    print(max(a + a - 1, a + b, b + b - 1))

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    print(max(a*2-1, a+b, b*2-1))

=======
Suggestion 5

def main():
    a,b = map(int,input().split())
    if a > b:
        print(a+a-1)
    elif a < b:
        print(b+b-1)
    else:
        print(a+b)

=======
Suggestion 6

def main():
    A, B = map(int, input().split())
    if A == B:
        print(A + B)
    else:
        print(max(A, B) + max(A, B) - 1)

=======
Suggestion 7

def main():
    a,b = map(int,input().split())
    if a == b:
        print(a+b)
    elif a > b:
        print(a+a-1)
    else:
        print(b+b-1)

=======
Suggestion 8

def main():
    A, B = map(int, input().split())
    print(max(A + A - 1, A + B, B + B - 1))

=======
Suggestion 9

def main():
    a,b = map(int,input().split())
    if a == b:
        print(a+b)
    elif a > b:
        print(a+a-1)
    else:
        print(b+b-1)

main()
