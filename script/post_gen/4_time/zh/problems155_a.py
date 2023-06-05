Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def is_triple_double(x, y, z):
    if x == y and x != z:
        return True
    elif x == z and x != y:
        return True
    elif y == z and y != x:
        return True
    else:
        return False

=======
Suggestion 2

def main():
    A, B, C = map(int, input().split())
    if A == B and A != C:
        print("Yes")
    elif A == C and A != B:
        print("Yes")
    elif B == C and B != A:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def solve():
    A,B,C = map(int,input().split())
    if A == B and A != C:
        print("Yes")
    elif A == C and A != B:
        print("Yes")
    elif B == C and B != A:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

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
Suggestion 5

def main():
    a,b,c = map(int,input().split())
    if a == b and a != c:
        print("是")
    elif a == c and a != b:
        print("是")
    elif b == c and b != a:
        print("是")
    else:
        print("否")

=======
Suggestion 6

def main():
    a, b, c = map(int, input().split())
    if a == b and b == c:
        print("No")
    elif a == b or b == c or c == a:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def is_diff(a, b, c):
    if a == b and a != c:
        return True
    elif a == c and a != b:
        return True
    elif b == c and b != a:
        return True
    else:
        return False

a, b, c = map(int, input().split())

=======
Suggestion 8

def main():
    a, b, c = map(int, input().split())
    if a == b != c or b == c != a or c == a != b:
        print('是')
    else:
        print('否')

=======
Suggestion 9

def is_diff(a,b,c):
    if a == b and b != c:
        return True
    elif a == c and b != c:
        return True
    elif b == c and a != b:
        return True
    else:
        return False
