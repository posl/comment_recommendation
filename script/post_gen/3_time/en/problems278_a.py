Synthesizing 10/10 solutions (Duplicates hidden)

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
        a.pop(0)
        a.append(0)
    print(*a)

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k):
        a.pop(0)
        a.append(0)
    print(" ".join(map(str, a)))

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k):
        a.append(a.pop(0))
    print(" ".join(map(str, a)))

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    for _ in range(k):
        a.pop(0)
        a.append(0)

    print(*a)

=======
Suggestion 6

def main():
    N,K = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(K):
        A.append(A.pop(0))
    print(' '.join(map(str, A)))

=======
Suggestion 7

def problem():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k):
        a.append(a.pop(0))
    print(' '.join(map(str, a)))
problem()

=======
Suggestion 8

def readinput():
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    return n,k,a

=======
Suggestion 9

def main():
    # Get input here
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # Calculate result here
    for i in range(k):
        a.append(a.pop(0))
    # Print output here
    print(' '.join(map(str, a)))
