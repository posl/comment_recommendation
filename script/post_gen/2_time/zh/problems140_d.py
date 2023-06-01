Synthesizing 10/10 solutions

=======
Suggestion 1

def problems140_c():
    pass

=======
Suggestion 2

def main():
    N = int(input())
    B = list(map(int, input().split()))
    A = [0] * N

    for i in range(N - 1):
        A[i] = max(B[i], B[i + 1])

    A[N - 1] = B[N - 2]

    print(sum(A))

=======
Suggestion 3

def maxSum(a):
    n = len(a)
    if n == 1:
        return a[0]
    elif n == 2:
        return max(a[0], a[1])
    else:
        if a[0] > a[1]:
            a[1] = a[0]
        for i in range(2, n):
            if a[i-1] > a[i]:
                a[i] = a[i-1]
        return a[n-1]

n = int(input())
b = list(map(int, input().split()))
a = [0] * n
for i in range(n-1):
    a[i] = b[i]
a[n-1] = b[n-2]

print(maxSum(a))

=======
Suggestion 4

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
Suggestion 5

def main():
    n = int(input())
    b = list(map(int, input().split()))
    a = []
    a.append(b[0])
    for i in range(n-2):
        a.append(min(b[i], b[i+1]))
    a.append(b[-1])
    print(sum(a))

=======
Suggestion 6

def solve():
    N = int(input())
    B = list(map(int,input().split()))
    A = [0] * N
    A[0] = B[0]
    A[N-1] = B[N-2]
    for i in range(1,N-1):
        A[i] = min(B[i-1],B[i])
    print(sum(A))

=======
Suggestion 7

def main():
    N = int(input())
    B = [int(i) for i in input().split()]
    A = [0 for i in range(N)]
    A[0] = B[0]
    A[-1] = B[-1]
    for i in range(1, N-1):
        A[i] = min(B[i-1], B[i])
    print(sum(A))

=======
Suggestion 8

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
Suggestion 9

def main():
    N = input()
    B = map(int, raw_input().split())
    A = [0] * N
    A[0] = B[0]
    A[N - 1] = B[N - 2]
    for i in xrange(1, N - 1):
        A[i] = min(B[i - 1], B[i])
    print sum(A)

=======
Suggestion 10

def main():
    n = int(input())
    b = list(map(int, input().split()))
    a = [0] * n
    a[0] = b[0]
    a[-1] = b[-1]
    for i in range(n - 2):
        a[i + 1] = min(b[i], b[i + 1])
    print(sum(a))
main()
