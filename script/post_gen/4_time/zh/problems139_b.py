Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b = map(int,input().split())
    if b%a == 0:
        print(int(b/a))
    else:
        print(int(b/a)+1)

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if a == 1:
        print(0)
    else:
        print((b-1) // (a - 1) + 1)

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    if B % A == 0:
        print(int(B/A))
    else:
        print(int(B/A)+1)

=======
Suggestion 4

def solve():
    a,b = map(int,input().split())
    c = 1
    while a < b:
        a += a-1
        c += 1
    print(c)

solve()

=======
Suggestion 5

def main():
    a,b = map(int,input().split())
    if b%a == 0:
        print(b//a - 1)
    else:
        print(b//a)

=======
Suggestion 6

def main():
    A,B = map(int,input().split())
    if B%A == 0:
        print(B//A)
    else:
        print(B//A + 1)

=======
Suggestion 7

def main():
    a, b = map(int, input().split())
    print((b + a - 3) // (a - 1))
