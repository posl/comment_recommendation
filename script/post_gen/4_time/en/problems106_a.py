Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a,b = map(int, input().split())
    print((a-1)*(b-1))

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    print(a*b - (a+b-1))

=======
Suggestion 3

def main():
    a,b = map(int, input().split())
    print(a*b - a - b + 1)

=======
Suggestion 4

def main():
    a,b = [int(x) for x in input().split()]
    print(a*b - (a+b) + 1)

=======
Suggestion 5

def main():
    a = input().split()
    b = int(a[0])
    c = int(a[1])
    print(b*c-1)

=======
Suggestion 6

def main():
    a,b = map(int,input().split())
    print(a*b-a-b+1)

main()

=======
Suggestion 7

def area(A, B):
    return A*B - (A+B-1)

=======
Suggestion 8

def area(a,b):
    return a*b

=======
Suggestion 9

def area(a,b):
    return a*b-1

=======
Suggestion 10

def area(l, b):
    return l*b
