Synthesizing 10/10 solutions (Duplicates hidden)

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
            p += 0
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
            P += 0
        elif A[i] == 3:
            P += 1
        elif A[i] == 4:
            P += 0
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
            P += 2
        elif A[i] == 3:
            P += 3
        elif A[i] == 4:
            P += 4
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
        else:
            P += 4
    print(P)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = 0
    for i in range(n):
        if a[i] == 1:
            p += 1
    print(p)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    S = [0] * 4
    for i in range(N):
        S[A[i]-1] += 1
    for i in range(4):
        if S[i] > 0:
            P += 1
    print(P)

=======
Suggestion 7

def solve():
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
Suggestion 8

def problem256_b():
    n = int(input())
    a = list(map(int,input().split()))
    p = 0
    for i in range(n):
        if a[i] == 1:
            p += 1
        elif a[i] == 2:
            p += 2
        elif a[i] == 3:
            p += 3
        elif a[i] == 4:
            p += 4
    print(p)

problem256_b()

=======
Suggestion 9

def main():
    #n = int(input())
    #a = input().split()
    #a = list(map(int, input().split()))
    n = 4
    a = [1, 1, 3, 2]
    #n = 3
    #a = [1, 1, 1]
    #n = 10
    #a = [2, 2, 4, 1, 1, 1, 4, 2, 2, 1]
    p = 0
    for i in range(n):
        p += a[i]
    print(p - n)
