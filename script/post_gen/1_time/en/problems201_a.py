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
    if A[0] - A[1] == A[1] - A[2]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    A = [int(s) for s in input().split()]
    A.sort()
    if A[2] - A[1] == A[1] - A[0]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    A = input().split()
    A = [int(i) for i in A]
    A.sort()
    if A[2]-A[1] == A[1]-A[0]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def is_arithmetic_sequence(a, b, c):
    if a == b and b == c:
        return True
    elif a == b or b == c or c == a:
        return False
    elif a - b == b - c or a - c == c - b or b - a == a - c:
        return True
    else:
        return False

a, b, c = map(int, input().split())
print("Yes" if is_arithmetic_sequence(a, b, c) else "No")

=======
Suggestion 6

def main():
    #input
    A = [int(i) for i in input().split()]

    #process
    A.sort()
    if A[2]-A[1] == A[1]-A[0]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def arithmetic_sequence(a,b,c):
    if a==b and b==c:
        return True
    elif a==b or b==c or a==c:
        return False
    else:
        if a>b and a>c:
            if b>c:
                if a-b==b-c:
                    return True
                else:
                    return False
            else:
                if a-c==c-b:
                    return True
                else:
                    return False
        elif b>a and b>c:
            if a>c:
                if b-a==a-c:
                    return True
                else:
                    return False
            else:
                if b-c==c-a:
                    return True
                else:
                    return False
        elif c>a and c>b:
            if a>b:
                if c-a==a-b:
                    return True
                else:
                    return False
            else:
                if c-b==b-a:
                    return True
                else:
                    return False

a,b,c=map(int,input().split())

=======
Suggestion 8

def main():
    # Read the data from the standard input
    A = map(int, raw_input().split())
    A.sort()
    # Check the condition
    if A[2] - A[1] == A[1] - A[0]:
        print "Yes"
    else:
        print "No"

=======
Suggestion 9

def main():
    # Get input data
    a = [int(x) for x in input().split()]
    # Sort the list
    a.sort()
    # Check if the difference between the first and second element is the
    # same as the difference between the second and third element
    if a[1] - a[0] == a[2] - a[1]:
        print("Yes")
    else:
        print("No")
