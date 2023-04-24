Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    if a == b and a != c:
        print("Yes")
    elif a == c and a != b:
        print("Yes")
    elif b == c and b != a:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def poor(A, B, C):
    if A == B and A != C:
        return True
    elif A == C and A != B:
        return True
    elif B == C and B != A:
        return True
    else:
        return False

=======
Suggestion 3

def poor(a, b, c):
    if a == b and a != c:
        return 'Yes'
    elif a == c and a != b:
        return 'Yes'
    elif b == c and b != a:
        return 'Yes'
    else:
        return 'No'

=======
Suggestion 4

def poor(a, b, c):
    if (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
        return "Yes"
    else:
        return "No"

=======
Suggestion 5

def poor(a,b,c):
    if a == b and a != c:
        return True
    elif a == c and a != b:
        return True
    elif b == c and b != a:
        return True
    else:
        return False

a,b,c = map(int, input().split())

=======
Suggestion 6

def isPoor(a,b,c):
    if a == b and b != c:
        return True
    elif a == c and c != b:
        return True
    elif b == c and c != a:
        return True
    else:
        return False

=======
Suggestion 7

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

main()

=======
Suggestion 8

def poor(a,b,c):
    if a == b:
        if b == c:
            return False
        else:
            return True
    elif a == c:
        if b == c:
            return False
        else:
            return True
    elif b == c:
        if a == c:
            return False
        else:
            return True
    else:
        return False

=======
Suggestion 9

def isPoor(a, b, c):
    if a != b and a != c and b != c:
        return "No"
    elif a == b and b == c:
        return "No"
    else:
        return "Yes"

=======
Suggestion 10

def isPoor(A, B, C):
    if A == B or A == C or B == C:
        return True
    else:
        return False
