Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(K):
        A.append(0)
        A.pop(0)
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
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k):
        a.append(0)
        a.pop(0)
    print(" ".join(map(str, a)))

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(K):
        A.append(0)
        del A[0]
    print(*A)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(K):
        A.append(0)
        A.pop(0)
    for i in A:
        print(i, end=' ')

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    for i in range(K):
        A.pop(0)
        A.append(0)
    
    print(' '.join(map(str, A)))

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if k >= n:
        print(*([0] * n))
    else:
        print(*a[k:], *([0] * k))

main()
