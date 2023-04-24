Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

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
Suggestion 3

def main():
    n = int(input())
    b = list(map(int, input().split()))
    a = [0]*n
    a[0] = b[0]
    a[-1] = b[-1]
    for i in range(1, n-1):
        a[i] = min(b[i-1], b[i])
    print(sum(a))

=======
Suggestion 4

def solve():
    N = int(input())
    B = list(map(int, input().split()))
    A = [0] * N
    A[0] = B[0]
    A[-1] = B[-1]
    for i in range(N-2):
        A[i+1] = min(B[i], B[i+1])
    print(sum(A))

=======
Suggestion 5

def solve():
    N = int(input())
    B = list(map(int, input().split()))
    A = [0] * N
    A[0] = B[0]
    A[N-1] = B[N-2]
    for i in range(N-2):
        A[i+1] = min(B[i], B[i+1])
    print(sum(A))
    return 0

=======
Suggestion 6

def main():
    N = int(input())
    B = list(map(int, input().split()))
    A = [B[0]]
    for i in range(N-2):
        A.append(min(B[i], B[i+1]))
    A.append(B[-1])
    print(sum(A))

main()

=======
Suggestion 7

def main():
    N = int(input())
    B = [int(x) for x in input().split()]
    A = [0] * N
    A[0] = B[0]
    A[N-1] = B[N-2]
    for i in range(1, N-1):
        A[i] = min(B[i-1], B[i])
    print(sum(A))

=======
Suggestion 8

def main():
    N = int(input())
    B = list(map(int,input().split()))
    B.append(0)
    A = [0] * N
    for i in range(N-1):
        A[i] = min(B[i], B[i+1])
    print(sum(A))

=======
Suggestion 9

def get_max_sum(a, b):
    max_sum = 0
    for i in range(len(b)):
        if i == 0:
            max_sum += b[i]
        else:
            max_sum += min(b[i], b[i-1])
    return max_sum
