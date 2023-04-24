Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A = list(map(int, input().split()))
    A.sort()
    if A[2] - A[1] == A[1] - A[0]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    A = [int(x) for x in input().split()]
    A.sort()
    if A[2] - A[1] == A[1] - A[0]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    a = list(map(int, input().split()))
    a.sort()
    if (a[2] - a[1]) == (a[1] - a[0]):
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def is_arithmetic_sequence(a, b, c):
    if a - b == b - c:
        return True
    elif a - c == c - b:
        return True
    elif b - a == a - c:
        return True
    elif b - c == c - a:
        return True
    elif c - a == a - b:
        return True
    elif c - b == b - a:
        return True
    else:
        return False

a, b, c = map(int, input().split())

=======
Suggestion 5

def main():
    A = input().split()
    A = [int(i) for i in A]
    A.sort()
    if A[2]-A[1]==A[1]-A[0]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def is_arithmetic_sequence(a, b, c):
    if a == b and b == c:
        return True
    elif a == b or b == c or a == c:
        return False
    else:
        return (a - b) == (b - c)

=======
Suggestion 7

def is_arithmetic_sequence(a,b,c):
    if (a-b) == (b-c):
        return True
    else:
        return False
