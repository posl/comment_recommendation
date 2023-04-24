Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(K):
        A.pop(0)
        A.append(0)
    print(*A)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k):
        a.pop(0)
        a.append(0)
    print(*a)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(K):
        A.pop(0)
        A.append(0)
    print(' '.join(map(str, A)))

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k):
        if i < n:
            a[i] = 0
        else:
            a.append(0)
    print(*a)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(K):
        if i < N:
            A[i] = 0
        else:
            A.append(0)
    print(' '.join(map(str, A)))

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(K):
        A.append(0)
        A.pop(0)
    print(*A)

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k):
        a.append(0)
        a.pop(0)
    print(*a)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    for i in range(K):
        A.append(0)
        A.pop(0)

    print(' '.join(map(str, A)))

=======
Suggestion 9

def main():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k):
        a.append(0)
        a.pop(0)
    print(' '.join(map(str,a)))
