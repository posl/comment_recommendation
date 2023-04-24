Synthesizing 10/10 solutions (Duplicates hidden)

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

=======
Suggestion 3

def main():
    S, T = input().split()
    A, B = map(int, input().split())
    U = input()
    if U == S:
        A -= 1
    elif U == T:
        B -= 1
    print(A, B)

=======
Suggestion 4

def main():
    S, T = input().split()
    A, B = map(int, input().split())
    U = input()
    if U == S:
        print(A-1, B)
    else:
        print(A, B-1)

=======
Suggestion 5

def main():
    S, T = input().split()
    A, B = map(int, input().split())
    U = input()
    if U == S:
        A -= 1
    if U == T:
        B -= 1
    print(A, B)
