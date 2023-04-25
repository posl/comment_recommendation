Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a,b = map(int, input().split())
    s = 0
    if a == 1:
        s += 300000
    elif a == 2:
        s += 200000
    elif a == 3:
        s += 100000
    if b == 1:
        s += 300000
    elif b == 2:
        s += 200000
    elif b == 3:
        s += 100000
    if a == 1 and b == 1:
        s += 400000
    print(s)
    return 0

=======
Suggestion 2

def main():
    A,B = map(int,input().split())
    C = A+B
    if C == 3:
        print(3)
    elif C == 2:
        print(4)
    elif C == 1:
        print(2)
    elif C == 0:
        print(0)
    else:
        print(1)

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    sol = 0
    if a == 1:
        sol += 300000
    elif a == 2:
        sol += 200000
    elif a == 3:
        sol += 100000
    if b == 1:
        sol += 300000
    elif b == 2:
        sol += 200000
    elif b == 3:
        sol += 100000
    if a == b == 1:
        sol += 400000
    print(sol)
main()

=======
Suggestion 4

def solve():
    A,B = map(int,input().split())
    C = A+B
    if C == 3:
        print(3)
    elif C == 2:
        print(4)
    elif C == 1:
        print(5)
    elif C == 0:
        print(0)
    else:
        print(6-C)

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    print(3 - a - b)

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    print(2*b-a)

=======
Suggestion 7

def solve():
    a, b = map(int, input().split())
    print(2*b - a)

=======
Suggestion 8

def main():
    a,b = map(int, input().split())
    c = a | b
    d = 7 - c
    print(d)

=======
Suggestion 9

def main():
    A,B = map(int,input().split())
    print(3 - (A+B)//2)

=======
Suggestion 10

def main():
    # get input
    a, b = map(int, input().split())
    # compute output
    c = a ^ b
    # output
    print(c)
