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
    A = list(map(int, input().split()))
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
    print("Yes" if a[2] - a[1] == a[1] - a[0] else "No")

=======
Suggestion 4

def arithmetic_sequence(A):
    A.sort()
    if A[2] - A[1] == A[1] - A[0]:
        return "Yes"
    else:
        return "No"

A = list(map(int, input().split()))
print(arithmetic_sequence(A))

=======
Suggestion 5

def isArithmeticSequence(A):
    A = sorted(A)
    if A[2] - A[1] == A[1] - A[0]:
        return True
    else:
        return False

=======
Suggestion 6

def main():
    a,b,c = map(int,input().split())
    if a+b == c+c or a+a == b+c or b+b == a+c:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def is_arithmetic_sequence(a):
    # a[0] = A_1, a[1] = A_2, a[2] = A_3
    # A_3 - A_2 = A_2 - A_1
    # A_3 - A_2 = A_

=======
Suggestion 8

def main():
    # Read data from stdin
    A = list(map(int, input().split()))
    # Sort the list
    A.sort()
    # Check if the difference between the first and second element is equal to the difference between the second and third element.
    if A[2] - A[1] == A[1] - A[0]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def isArithmeticSequence(a,b,c):
    return (a - b) == (b - c)
