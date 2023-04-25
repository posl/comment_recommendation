Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S = list(map(int, input().split()))
    A = [0] * N
    A[0] = S[0]
    for i in range(1, N):
        A[i] = S[i] - S[i-1]
    print(*A)

=======
Suggestion 2

def main():
    N = int(input())
    S = list(map(int, input().split()))
    A = [0] * N
    A[0] = S[0]
    for i in range(1, N):
        A[i] = S[i] - S[i-1]
    print(' '.join(map(str, A)))

=======
Suggestion 3

def main():
    n = int(input())
    s = list(map(int, input().split()))
    a = [0] * n
    a[0] = s[0]
    for i in range(1, n):
        a[i] = s[i] - s[i - 1]
    print(' '.join(map(str, a)))

=======
Suggestion 4

def main():
    n = int(input())
    s = list(map(int, input().split()))
    a = [0]*n
    a[0] = s[0]
    for i in range(1, n):
        a[i] = s[i] - s[i-1]
    print(*a)

=======
Suggestion 5

def main():
    N = int(input())
    S = [int(x) for x in input().split()]
    A = [0] * N
    A[0] = S[0]
    for i in range(1, N):
        A[i] = S[i] - S[i-1]
    print(" ".join(map(str, A)))

=======
Suggestion 6

def main():
    n = int(input())
    s = [int(x) for x in input().split()]
    a = [0 for i in range(n)]
    a[0] = s[0]
    for i in range(1, n):
        a[i] = s[i] - s[i-1]
    print(' '.join([str(x) for x in a]))

=======
Suggestion 7

def main():
    n = int(input())
    s = list(map(int, input().split()))
    a = [0] * n
    for i in range(n):
        if i % 2 == 0:
            a[0] += s[i]
        else:
            a[0] -= s[i]
    a[0] = a[0] // 2
    for i in range(1, n):
        a[i] = s[i - 1] - a[i - 1]
    print(*a)
