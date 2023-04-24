Synthesizing 10/10 solutions

=======
Suggestion 1

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
Suggestion 2

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
Suggestion 3

def poor(a, b, c):
    if a == b and b != c:
        return True
    elif a == c and c != b:
        return True
    elif b == c and c != a:
        return True
    else:
        return False

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
    return

=======
Suggestion 5

def main():
    a, b, c = map(int, input().split())
    if a == b and a != c or a == c and a != b or b == c and b != a:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    a, b, c = input().split()
    if a == b and a != c:
        print('Yes')
    elif a == c and a != b:
        print('Yes')
    elif b == c and b != a:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def poor(num1, num2, num3):
    if num1 == num2 and num1 != num3:
        return True
    elif num1 == num3 and num1 != num2:
        return True
    elif num2 == num3 and num2 != num1:
        return True
    else:
        return False

=======
Suggestion 8

def poor(a, b, c):
    if a == b and b != c:
        return True
    elif a == c and a != b:
        return True
    elif b == c and b != a:
        return True
    else:
        return False

=======
Suggestion 9

def poor(A,B,C):
    if (A == B and A != C) or (A == C and A != B) or (B == C and B != A):
        return "Yes"
    else:
        return "No"

A,B,C = map(int,input().split())
print(poor(A,B,C))

=======
Suggestion 10

def main():
    a,b,c = map(int, input().split())
    if a == b and b != c:
        print("Yes")
    elif a == c and a != b:
        print("Yes")
    elif b == c and b != a:
        print("Yes")
    else:
        print("No")
