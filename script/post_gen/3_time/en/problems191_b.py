Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] != x:
            print(a[i], end=' ')

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    for a in A:
        if a != X:
            print(a, end=' ')

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        if A[i] != X:
            print(A[i], end = " ")

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] != x:
            print(a[i], end=' ')
    print()

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        if A[i] != X:
            print(A[i], end=" ")
    print()

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    for a in A:
        if a != X:
            print(a, end=" ")
    print()

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    print(' '.join(map(str, [a for a in A if a != X])))

=======
Suggestion 8

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    for i in a:
        if i != x:
            print(i, end = " ")

=======
Suggestion 9

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A_ = [a for a in A if a != X]
    print(" ".join(map(str, A_)))

=======
Suggestion 10

def main():
    # read input
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    # remove elements equal to x
    a = [e for e in a if e != x]
    # print the remaining elements
    print(' '.join(map(str, a)))
