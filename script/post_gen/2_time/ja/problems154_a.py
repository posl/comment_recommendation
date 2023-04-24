Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

def main():
    S, T = input().split()
    A, B = map(int, input().split())
    U = input()
    if U == S:
        print(A-1, B)
    else:
        print(A, B-1)

=======
Suggestion 3

def main():
    s, t = input().split()
    a, b = map(int, input().split())
    u = input()
    if u == s:
        print(a - 1, b)
    else:
        print(a, b - 1)

=======
Suggestion 4

def main():
    S, T = input().split()
    A, B = map(int, input().split())
    U = input()
    if U == S:
        print(A-1, B)
    elif U == T:
        print(A, B-1)

=======
Suggestion 5

def main():
    s,t = input().split()
    a,b = map(int, input().split())
    u = input()
    if s == u:
        a -= 1
    else:
        b -= 1
    print(a,b)

=======
Suggestion 6

def main():
    S,T = input().split()
    A,B = map(int, input().split())
    U = input()
    if U == S:
        A -= 1
    elif U == T:
        B -= 1
    print(A,B)

=======
Suggestion 7

def main():
    # 標準入力受け取り
    s, t = input().split()
    a, b = map(int, input().split())
    u = input()

    if u == s:
        a -= 1
    else:
        b -= 1

    print(a, b)

=======
Suggestion 8

def solve():
    # -*- coding: utf-8 -*-
    s,t = input().split()
    a,b = map(int,input().split())
    u = input()
    if u == s:
        a -= 1
    else:
        b -= 1
    print(a,b)
solve()
