Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    max_a = max(a)
    max_a_index = a.index(max_a)
    for i in range(n):
        if i == max_a_index:
            print(sorted(a, reverse=True)[1])
        else:
            print(max_a)

=======
Suggestion 2

def main():
    n = int(input())
    a = [int(input()) for i in range(n)]
    max_a = max(a)
    for i in range(n):
        if a[i] == max_a:
            print(max(a[:i] + a[i+1:]))
        else:
            print(max_a)

=======
Suggestion 3

def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    a_max = max(a)
    a_max_index = a.index(a_max)
    for i in range(n):
        if i == a_max_index:
            print(max(a[:i] + a[i+1:]))
        else:
            print(a_max)

=======
Suggestion 4

def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    max_a = max(a)
    max_index = a.index(max_a)
    for i in range(n):
        if i == max_index:
            print(max(a[:i] + a[i+1:]))
        else:
            print(max_a)

=======
Suggestion 5

def main():
    n = int(input())
    a = [int(input()) for i in range(n)]
    a_max = max(a)
    for i in range(n):
        if a[i] == a_max:
            print(sorted(a)[-2])
        else:
            print(a_max)

=======
Suggestion 6

def main():
    n = int(input())
    a = [int(input()) for i in range(n)]
    a_max = max(a)
    a_max2 = sorted(a)[-2]
    for i in a:
        if i == a_max:
            print(a_max2)
        else:
            print(a_max)

=======
Suggestion 7

def main():
    N = int(input())
    A = [int(input()) for i in range(N)]
    A.sort()
    for i in range(N):
        if i != N-1:
            print(A[N-1])
        else:
            print(A[N-2])

=======
Suggestion 8

def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    maxA = max(A)
    for a in A:
        if a == maxA:
            print(max(A[:A.index(a)] + A[A.index(a)+1:]))
        else:
            print(maxA)

=======
Suggestion 9

def main():
    N = int(input())
    A = [int(input()) for i in range(N)]
    maxA = max(A)
    maxAind = A.index(maxA)
    for i in range(N):
        if i == maxAind:
            print(sorted(A[:-1])[-1])
        else:
            print(maxA)
