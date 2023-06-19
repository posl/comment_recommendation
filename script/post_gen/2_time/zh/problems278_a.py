Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    for i in range(k):
        a.pop(0)
        a.append(0)
    print(*a)

=======
Suggestion 2

def problems278_a():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(K):
        A.pop(0)
        A.append(0)
    print(' '.join(map(str, A)))

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

def solution():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k):
        a.pop(0)
        a.append(0)
    print(*a)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(K):
        A.append(A[0])
        A.pop(0)
        A.append(0)
        A.pop(0)
    print(" ".join(map(str, A)))

=======
Suggestion 6

def problems278_a():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(k):
        a.pop(0)
        a.append(0)
    print(*a)

problems278_a()

=======
Suggestion 7

def problems278_a():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k):
        a.pop(0)
        a.append(0)
    print(' '.join(map(str, a)))

=======
Suggestion 8

def get_input():
    input = raw_input()
    input = input.split(' ')
    N = int(input[0])
    K = int(input[1])
    input = raw_input()
    input = input.split(' ')
    A = [int(i) for i in input]
    return N, K, A

=======
Suggestion 9

def problems278_a():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(K):
        A.append(0)
        del A[0]
    print(' '.join(map(str, A)))
