Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    if (A * B) % 2 == 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    if (A == 1 and B == 2) or (A == 2 and B == 1):
        print("No")
    else:
        print("Yes")

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if a == 1:
        if b == 1:
            print('No')
        else:
            print('Yes')
    elif a == 2:
        if b == 2:
            print('No')
        else:
            print('Yes')
    else:
        if b == 3:
            print('No')
        else:
            print('Yes')

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    if (A*B)%2 == 1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    if a == 1 or b == 1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    input = sys.stdin.readline
    A, B = map(int, input().split())
    if (A * B) % 2 == 0:
        print("No")
    else:
        print("Yes")

=======
Suggestion 7

def main():
    A,B = map(int,input().split())
    if A*B%2 == 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    a,b = map(int,input().split())
    if a*b%2 == 0:
        print('No')
    else:
        print('Yes')

=======
Suggestion 9

def is_odd(a, b):
    if (a * b) % 2 == 0:
        return "No"
    else:
        return "Yes"

=======
Suggestion 10

def main():
    #input
    A,B = map(int,input().split())
    #output
    if A*B%2 == 0:
        print("No")
    else:
        print("Yes")
