Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def calc(a, b):
    if a >= b:
        return 1
    else:
        if b % a == 0:
            return b / a
        else:
            return b / a + 1

=======
Suggestion 2

def main():
    a,b = map(int, input().split())
    if b%a == 0:
        print(0)
    else:
        print(a-b%a)

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if b % a == 0:
        print(b // a)
    else:
        print(b // a + 1)

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    if b % a == 0:
        print(b // a - 1)
    else:
        print(b // a)

=======
Suggestion 5

def solve(a,b):
    if b % a == 0:
        return 0
    else:
        return 1

=======
Suggestion 6

def solve():
    a,b = map(int,input().split())
    if b % a == 0:
        print(b//a)
    else:
        print(b//a+1)

=======
Suggestion 7

def main():
    A,B = map(int,input().split())
    if B%A == 0:
        print(int(B/A))
    else:
        print(int(B/A)+1)

=======
Suggestion 8

def main():
    A, B = map(int, input().split())
    if B % A == 0:
        print(B // A)
    else:
        print(B // A + 1)
