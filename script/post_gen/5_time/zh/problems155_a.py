Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def is_triple_double(x, y, z):
    if x == y and y != z:
        return True
    if x == z and x != y:
        return True
    if y == z and y != x:
        return True
    return False

x, y, z = map(int, input().split())

=======
Suggestion 2

def is_triple_double(a, b, c):
    if a == b and a != c:
        return True
    elif a == c and a != b:
        return True
    elif b == c and b != a:
        return True
    else:
        return False

=======
Suggestion 3

def main():
    a, b, c = map(int, input().split())
    if a == b and b != c:
        print("是")
    elif b == c and c != a:
        print("是")
    elif a == c and c != b:
        print("是")
    else:
        print("否")

=======
Suggestion 4

def is_triple_double(A, B, C):
    if A == B and B != C:
        return "是"
    elif B == C and C != A:
        return "是"
    elif C == A and A != B:
        return "是"
    else:
        return "否"

=======
Suggestion 5

def main():
    a,b,c = map(int,input().split())
    if a == b and b != c:
        print("是")
    elif a == c and b != c:
        print("是")
    elif b == c and a != c:
        print("是")
    else:
        print("否")

=======
Suggestion 6

def is_difference(a,b,c):
    if a == b and b != c:
        return True
    elif a == c and a != b:
        return True
    elif b == c and a != b:
        return True
    else:
        return False

=======
Suggestion 7

def problem155_a():
    a, b, c = map(int, input().split())
    if a == b:
        if a != c:
            print("Yes")
        else:
            print("No")
    elif a == c:
        print("Yes")
    elif b == c:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def is_diff(a,b,c):
    if a == b and b != c:
        return True
    elif b == c and c != a:
        return True
    elif c == a and a != b:
        return True
    else:
        return False
