Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    b = list(map(int, input().split()))
    a = [0]*n
    a[0] = b[0]
    a[n-1] = b[n-2]
    for i in range(1, n-1):
        a[i] = min(b[i-1], b[i])
    print(sum(a))

=======
Suggestion 2

def get_max_sum(n, b):
    a = [0] * n
    a[0] = b[0]
    for i in range(1, n-1):
        a[i] = max(b[i], b[i-1])
    a[n-1] = b[n-2]
    return sum(a)

=======
Suggestion 3

def main():
    n = int(input())
    b = list(map(int, input().split()))
    a = [0] * n
    a[0] = b[0]
    a[-1] = b[-1]
    for i in range(n-2):
        a[i+1] = min(b[i], b[i+1])
    print(sum(a))

=======
Suggestion 4

def maxsum(n, b):
    a = [0 for i in range(n)]
    a[0] = b[0]
    for i in range(1, n-1):
        a[i] = max(b[i], b[i-1])
    a[-1] = b[-1]
    return sum(a)

=======
Suggestion 5

def main():
    N = int(input())
    B = list(map(int, input().split()))
    A = [0]*N
    A[0] = B[0]
    for i in range(1, N-1):
        A[i] = max(B[i], B[i-1])
    A[-1] = B[-1]
    print(sum(A))

=======
Suggestion 6

def main():
    n = int(input())
    b = list(map(int, input().split()))
    a = [0] * n
    a[0] = b[0]
    for i in range(n-2):
        a[i+1] = min(b[i], b[i+1])
    a[n-1] = b[n-2]
    print(sum(a))

=======
Suggestion 7

def solve(n, b):
    a = [0] * n
    a[0] = b[0]
    for i in range(1, n-1):
        a[i] = max(b[i-1], b[i])
    a[n-1] = b[n-2]
    return sum(a)

=======
Suggestion 8

def main():
    N = int(input())
    B = list(map(int, input().split()))
    A = [0] * N
    A[0] = B[0]
    A[N-1] = B[N-2]
    for i in range(1, N-1):
        A[i] = min(B[i-1], B[i])
    print(sum(A))

=======
Suggestion 9

def main():
    n = int(input())
    b = list(map(int, input().split()))
    a = [0 for i in range(n)]
    a[0] = b[0]
    a[n-1] = b[n-2]
    for i in range(n-2):
        a[i+1] = min(b[i], b[i+1])
    print(sum(a))
