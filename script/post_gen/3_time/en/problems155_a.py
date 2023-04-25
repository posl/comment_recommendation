Synthesizing 10/10 solutions

=======
Suggestion 1

def poor(A, B, C):
    if A == B and A != C:
        return True
    elif A == C and A != B:
        return True
    elif B == C and B != A:
        return True
    else:
        return False

A, B, C = map(int, input().split())

=======
Suggestion 2

def main():
    A, B, C = map(int, input().split())
    if (A == B and A != C) or (A == C and A != B) or (B == C and B != A):
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def isPoor(a,b,c):
    if a==b and a!=c:
        return True
    elif a==c and a!=b:
        return True
    elif b==c and b!=a:
        return True
    else:
        return False

=======
Suggestion 4

def poor(a,b,c):
    if a == b and a != c:
        return True
    if a == c and a != b:
        return True
    if b == c and b != a:
        return True
    return False

a,b,c = map(int, input().split())

=======
Suggestion 5

def poor(a,b,c):
    if a == b and a != c:
        return True
    if a == c and a != b:
        return True
    if b == c and b != a:
        return True
    return False

=======
Suggestion 6

def poor(a,b,c):
    if a==b and b!=c:
        return "Yes"
    elif a==c and c!=b:
        return "Yes"
    elif b==c and c!=a:
        return "Yes"
    else:
        return "No"

a,b,c=map(int,input().split())
print(poor(a,b,c))

=======
Suggestion 7

def poor(a,b,c):
    if a == b and a != c:
        return 'Yes'
    elif b == c and b != a:
        return 'Yes'
    elif a == c and a != b:
        return 'Yes'
    else:
        return 'No'

=======
Suggestion 8

def poor(a,b,c):
    if a == b and b != c:
        return "Yes"
    elif a == c and b != c:
        return "Yes"
    elif b == c and a != c:
        return "Yes"
    else:
        return "No"

=======
Suggestion 9

def checkPoor(a, b, c):
    if a == b and a != c:
        return True
    elif b == c and b != a:
        return True
    elif a == c and a != b:
        return True
    else:
        return False

=======
Suggestion 10

def isPoor(a,b,c):
    return (a==b and a!=c) or (a==c and a!=b) or (b==c and b!=a)
