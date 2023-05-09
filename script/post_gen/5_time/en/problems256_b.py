Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = 0
    for i in range(n):
        if a[i] == 1:
            p += 1
        elif a[i] == 2:
            p += 0
        elif a[i] == 3:
            p += 1
        elif a[i] == 4:
            p += 2
    print(p)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        if A[i] == 1:
            P += 1
        elif A[i] == 2:
            P += 2
        elif A[i] == 3:
            P += 3
        elif A[i] == 4:
            P += 4
    print(P)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        if A[i] == 1:
            P += 1
        elif A[i] == 2:
            P += 0
        elif A[i] == 3:
            P += 1
        elif A[i] == 4:
            P += 2
        else:
            P += 0
    print(P)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        if A[i] == 1:
            P += 1
        elif A[i] == 2:
            P += 2
        elif A[i] == 3:
            P += 3
        elif A[i] == 4:
            P += 4
    print(P)
main()

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        if A[i] == 1:
            P += 1
        elif A[i] == 2:
            P += 0
        elif A[i] == 3:
            P += 1
        elif A[i] == 4:
            P += 2
    print(P)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        if A[i] == 1:
            P += 1
        elif A[i] == 2:
            P += 0
        elif A[i] == 3:
            P += 1
        elif A[i] == 4:
            P += 0
    print(P)

=======
Suggestion 7

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    p = 0
    for i in range(n):
        if a[i] == 1:
            p += 1
        elif a[i] == 2:
            p += 0
        elif a[i] == 3:
            p += 1
        elif a[i] == 4:
            p += 0
    print(p)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int,input().split()))
    p = 0
    for i in range(n):
        if a[i] == 1:
            p += 1
        elif a[i] == 2:
            p += 0
        elif a[i] == 3:
            p += 1
        else:
            p += 2
    print(p)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = 0
    for i in range(n):
        if 1 == a[i]:
            p += 1
        elif 2 == a[i]:
            p += 0
        elif 3 == a[i]:
            p += 0
        elif 4 == a[i]:
            p += 1
    print(p)

=======
Suggestion 10

def solve(n, a):
    p = 0
    for i in range(n):
        p += a[i] - 1
    return p
