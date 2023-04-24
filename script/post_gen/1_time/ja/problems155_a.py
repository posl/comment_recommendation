Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    if a == b and a != c:
        print('Yes')
    elif a == c and a != b:
        print('Yes')
    elif b == c and b != a:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    if a == b == c:
        print("No")
    elif a == b or b == c or c == a:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    a, b, c = map(int, input().split())
    if a == b and b != c:
        print('Yes')
    elif a == c and b != c:
        print('Yes')
    elif b == c and a != c:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    A, B, C = map(int, input().split())
    if A == B and A != C:
        print("Yes")
    elif B == C and B != A:
        print("Yes")
    elif C == A and C != B:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    a, b, c = map(int, input().split())
    if a == b and b != c:
        print("Yes")
    elif a == c and a != b:
        print("Yes")
    elif b == c and a != b:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    a, b, c = map(int, input().split())
    if a == b:
        if a == c:
            print("No")
        else:
            print("Yes")
    elif a == c:
        print("Yes")
    elif b == c:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    a,b,c = map(int,input().split())
    if a == b and b != c:
        print("Yes")
    elif a == c and b != c:
        print("Yes")
    elif b == c and a != c:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    a, b, c = map(int, input().split())

    if a == b:
        if a == c:
            print("No")
        else:
            print("Yes")
    elif b == c:
        print("Yes")
    elif a == c:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def check(a, b, c):
    if a == b:
        if a != c:
            return True
        else:
            return False
    elif b == c:
        if b != a:
            return True
        else:
            return False
    elif c == a:
        if c != b:
            return True
        else:
            return False
    else:
        return False
