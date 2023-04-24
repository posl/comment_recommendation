Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    B = list(map(int, input().split()))
    A = [0] * N
    A[0] = B[0]
    A[-1] = B[-1]
    for i in range(1, N-1):
        A[i] = min(B[i-1], B[i])
    print(sum(A))

=======
Suggestion 2

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
Suggestion 3

def main():
    N = int(input())
    B = list(map(int, input().split()))
    A = [0]*N
    A[0] = B[0]
    A[-1] = B[-1]
    for i in range(1, N-1):
        A[i] = min(B[i], B[i-1])
    print(sum(A))

=======
Suggestion 4

def solve(N, B):
    A = [0] * N
    A[0] = B[0]
    A[-1] = B[-1]
    for i in range(1, N-1):
        A[i] = min(B[i-1], B[i])
    return A

N = int(input())
B = list(map(int, input().split()))
A = solve(N, B)
print(sum(A))

=======
Suggestion 5

def main():
    N = int(input())
    B = [int(i) for i in input().split()]
    A = [0 for i in range(N)]
    A[0] = B[0]
    A[N-1] = B[N-2]
    for i in range(1,N-1):
        A[i] = min(B[i-1],B[i])
    print(sum(A))
