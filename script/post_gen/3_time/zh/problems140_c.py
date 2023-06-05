Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(n, b):
    a = [0] * n
    for i in range(n-1):
        if b[i] > b[i+1]:
            a[i+1] = b[i+1]
        else:
            a[i+1] = b[i]
    return sum(a)

=======
Suggestion 2

def main():
    n = int(input())
    b = [int(x) for x in input().split()]
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
    a = [0] * n
    a[0] = b[0]
    a[n - 1] = b[n - 2]
    for i in range(n - 2):
        a[i + 1] = min(b[i], b[i + 1])
    print(sum(a))

=======
Suggestion 4

def main():
    n = int(input())
    b = list(map(int, input().split()))

    a = [0] * n
    a[0] = b[0]
    a[-1] = b[-1]
    for i in range(n-2):
        a[i+1] = min(b[i], b[i+1])

    print(sum(a))

main()

=======
Suggestion 5

def max_sum(N, B):
    A = [0] * N
    A[0] = B[0]
    for i in range(N-2):
        A[i+1] = max(B[i], B[i+1])
    A[N-1] = B[N-2]
    return sum(A)

=======
Suggestion 6

def main():
    n = int(input())
    b = list(map(int, input().split()))
    b.append(0)
    a = [0 for i in range(n)]
    a[0] = b[0]
    for i in range(1, n):
        a[i] = min(b[i - 1], b[i])
    print(sum(a))

=======
Suggestion 7

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
Suggestion 8

def find_max(A):
    max = A[0]
    for i in range(1,len(A)):
        if A[i] > max:
            max = A[i]
    return max

=======
Suggestion 9

def max_sum(A, B):
    A[0] = B[0]
    for i in range(1, len(A)):
        A[i] = max(B[i-1], B[i])
    return sum(A)

N = int(input())
B = list(map(int, input().split()))
A = [0] * N
print(max_sum(A, B))

=======
Suggestion 10

def sum_max(a):
    s = 0
    for i in range(len(a)):
        s += a[i]
    return s
