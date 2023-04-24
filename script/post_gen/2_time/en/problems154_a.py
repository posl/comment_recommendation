Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S, T = input().split()
    A, B = map(int, input().split())
    U = input()
    if U == S:
        A -= 1
    else:
        B -= 1
    print(A, B)

=======
Suggestion 2

def main():
    s, t = input().split()
    a, b = map(int, input().split())
    u = input()
    if u == s:
        a -= 1
    else:
        b -= 1
    print(a, b)

main()

=======
Suggestion 3

def main():
    s, t = input().split()
    a, b = map(int, input().split())
    u = input()
    if u == s:
        a -= 1
    else:
        b -= 1
    print(a, b)

=======
Suggestion 4

def main():
    S, T = input().split()
    A, B = map(int, input().split())
    U = input()
    if S == U:
        A -= 1
    elif T == U:
        B -= 1
    print(A, B)

=======
Suggestion 5

def main():
    S, T = input().split()
    A, B = map(int, input().split())
    U = input()
    if U == S:
        print(A-1, B)
    else:
        print(A, B-1)

=======
Suggestion 6

def main():
    S, T = input().split()
    A, B = map(int, input().split())
    U = input()

    if S == U:
        A -= 1
    else:
        B -= 1

    print(A, B)

=======
Suggestion 7

def main():
    S, T = input().split()
    A, B = map(int, input().split())
    U = input()
    if S == U:
        print(A-1, B)
    else:
        print(A, B-1)

=======
Suggestion 8

def main():
    S, T = input().split()
    A, B = map(int, input().split())
    U = input()
    if U == S:
        A = A - 1
    else:
        B = B - 1
    print(A, B)

=======
Suggestion 9

def main():
    S, T = input().split()
    A, B = map(int, input().split())
    U = input()
    if S == U:
        print(A-1, B)
    elif T == U:
        print(A, B-1)

=======
Suggestion 10

def main():
    # Get input
    S, T = input().split()
    A, B = map(int, input().split())
    U = input()

    # Check if U is S or T
    if U == S:
        A -= 1
    else:
        B -= 1

    # Print the answer
    print(A, B)
