Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if (a * b) % 2 == 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if a * b % 2 == 1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if a * b % 2 == 0:
        print('No')
    else:
        print('Yes')

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    if A % 2 == 1 and B % 2 == 1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    # input
    A, B = map(int, input().split())

    # compute

    # output
    if A*B%2 == 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def solve():
    a, b = map(int, input().split())
    if a * b % 2 == 1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    a, b = map(int, input().split())
    print("Yes" if a * b % 2 == 1 else "No")

=======
Suggestion 8

def solve():
    a,b = map(int,input().split())
    if a*b%2 == 0:
        print('No')
    else:
        print('Yes')

=======
Suggestion 9

def main():
    A,B = map(int,input().split())
    if A*B%2==0:
        print("No")
    else:
        print("Yes")

=======
Suggestion 10

def odd(a,b):
    c=a*b
    if c%2==1:
        print('Yes')
    else:
        print('No')

odd(3,1)
odd(1,2)
odd(2,2)
