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
    for _ in range(k):
        a.pop(0)
        a.append(0)
    print(*a)

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k):
        a.append(0)
        a.pop(0)
    print(*a)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k):
        a[i] = 0
    print(*a)

=======
Suggestion 5

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(k):
        a.append(0)
        a.pop(0)
    print(' '.join(map(str,a)))

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    for i in range(K):
        if i == 0:
            A = A[1:]
            A.append(0)
        else:
            A = A[1:]
            A.append(0)

    print(' '.join(map(str, A)))

=======
Suggestion 7

def main():
    # input
    N, K = map(int, input().split())
    As = list(map(int, input().split()))

    # compute
    for i in range(K):
        As.append(0)
        As.pop(0)

    # output
    print(' '.join(map(str, As)))

=======
Suggestion 8

def main():
    #input
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #operation
    for i in range(K):
        A[i] = 0
    #output
    print(*A)
