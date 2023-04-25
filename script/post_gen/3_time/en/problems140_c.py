Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    B = list(map(int, input().split()))
    A = [0] * N
    A[0] = B[0]
    A[-1] = B[-1]
    for i in range(1,N-1):
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
    n = int(input())
    b = list(map(int, input().split()))
    a = [0] * n
    a[0] = b[0]
    a[n-1] = b[n-2]
    for i in range(1, n-1):
        a[i] = min(b[i-1], b[i])
    print(sum(a))

=======
Suggestion 4

def main():
    n = int(input())
    b = list(map(int, input().split()))
    a = [0] * n
    a[0] = b[0]
    a[n-1] = b[n-2]
    for i in range(1, n-1):
        a[i] = min(b[i-1], b[i])
    print(sum(a))

main()

=======
Suggestion 5

def solve():
    N = int(input())
    B = list(map(int, input().split()))
    A = [0] * N
    A[0] = B[0]
    A[-1] = B[-1]
    for i in range(1, N-1):
        A[i] = min(A[i-1], B[i])
    print(sum(A))

=======
Suggestion 6

def main():
    n = int(input())
    b = list(map(int,input().split()))
    a = [0] * n
    a[0] = b[0]
    a[-1] = b[-1]
    for i in range(1,n-1):
        a[i] = min(b[i-1],b[i])
    print(sum(a))

=======
Suggestion 7

def solve():
    N = int(input())
    B = list(map(int, input().split()))
    A = [B[0]]
    for i in range(1, N-1):
        A.append(min(B[i-1], B[i]))
    A.append(B[-1])
    print(sum(A))
