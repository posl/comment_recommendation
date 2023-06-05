Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    #print("280_b")
    n = int(input())
    s = list(map(int,input().split()))
    a = [0 for i in range(n)]
    a[0] = s[0]
    for i in range(1,n):
        a[i] = s[i] - s[i-1]
    print(*a)

=======
Suggestion 2

def main():
    N = int(input())
    S = list(map(int, input().split()))
    A = [0]*N
    A[0] = S[0]
    for i in range(1, N):
        A[i] = S[i] - S[i-1]
    print(*A)

=======
Suggestion 3

def main():
    N = int(input())
    S = list(map(int, input().split()))
    A = [0] * N
    A[0] = S[0]
    for i in range(1, N):
        A[i] = S[i] - S[i - 1]
    print(" ".join(map(str, A)))

=======
Suggestion 4

def solve(N, S):
    A = [0] * N
    A[0] = S[0]
    for i in range(1, N):
        A[i] = S[i] - S[i - 1]
    return A

=======
Suggestion 5

def main():
    n = int(input())
    s = list(map(int, input().split()))
    a = [0] * n
    a[0] = s[0]
    for i in range(1, n):
        a[i] = s[i] - s[i - 1]
    print(' '.join(map(str, a)))

=======
Suggestion 6

def main():
    n = int(input())
    s = [int(i) for i in input().split()]
    a = [0 for i in range(n)]
    a[0] = s[0]
    for i in range(1, n):
        a[i] = s[i] - s[i-1]
    print(' '.join([str(i) for i in a]))

=======
Suggestion 7

def solve(n, s):
    sum_s = sum(s)
    sum_a = 0
    a = [0] * n
    for i in range(n):
        if i % 2 == 0:
            a[i] = max(-sum_a, sum_s - sum_a)
        else:
            a[i] = -max(-sum_a, sum_s - sum_a)
        sum_a += a[i]
    return a

=======
Suggestion 8

def main():
    n = int(input())
    s = list(map(int, input().split()))
    a = [0] * n
    a[0] = s[0]
    for i in range(1, n):
        a[i] = s[i] - s[i-1]
    print(*a)
