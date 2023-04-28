Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k):
        a.pop(0)
        a.append(0)
    print(' '.join(map(str, a)))

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k):
        a.append(a.pop(0))
    print(' '.join(map(str, a)))

=======
Suggestion 3

def problems278_a():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k):
        a.pop(0)
        a.append(0)
    print(*a)

=======
Suggestion 4

def problems278_a():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(K):
        A.pop(0)
        A.append(0)
    print(*A)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k):
        a.append(a.pop(0))
    print(*a)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    for i in range(K):
        A.append(A.pop(0))

    print(' '.join(map(str, A)))

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(K):
        A.append(A.pop(0))
        A.append(0)
    print(" ".join(map(str, A)))

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(K):
        A.append(A.pop(0))
        A.append(0)
    print(*A)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(K):
        A.append(A.pop(0))
        A.append(0)
    A.pop()
    print(' '.join(map(str, A)))

=======
Suggestion 10

def problem():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k):
        a.append(a.pop(0))
    print(' '.join(map(str, a)))

problem()
