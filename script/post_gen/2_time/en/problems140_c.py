Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    B = list(map(int, input().split()))
    A = [0] * N
    A[0] = B[0]
    A[-1] = B[-1]
    for i in range(1, N - 1):
        A[i] = min(B[i - 1], B[i])
    print(sum(A))

=======
Suggestion 2

def main():
    N = int(input())
    B = list(map(int, input().split()))
    A = [0] * N
    A[0] = B[0]
    A[-1] = B[-1]
    for i in range(N-2):
        A[i+1] = min(B[i], B[i+1])
    print(sum(A))

=======
Suggestion 3

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
Suggestion 4

def solve(N, B):
    A = [0] * N
    A[0] = B[0]
    A[-1] = B[-1]
    for i in range(1, N-1):
        A[i] = min(B[i-1], B[i])
    return sum(A)

N = int(input())
B = list(map(int, input().split()))
print(solve(N, B))

=======
Suggestion 5

def solve(n, b):
    a = [0] * n
    a[0] = b[0]
    a[-1] = b[-1]
    for i in range(1, n-1):
        a[i] = min(b[i], a[i-1])
    return sum(a)

=======
Suggestion 6

def max_sum(A):
    N = len(A)
    B = [0] * N
    B[0] = A[0]
    B[N-1] = A[N-2]
    for i in range(1,N-1):
        B[i] = min(A[i-1], A[i])
    return sum(B)

N = int(input())
A = list(map(int, input().split()))
print(max_sum(A))
