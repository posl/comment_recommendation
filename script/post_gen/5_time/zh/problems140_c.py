Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N = int(input())
    B = list(map(int, input().split()))
    ans = B[0] + B[-1]
    for i in range(N - 2):
        ans += min(B[i], B[i + 1])
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    B = list(map(int, input().split()))
    A = [0] * N
    A[0] = B[0]
    for i in range(N-2):
        A[i+1] = min(B[i], B[i+1])
    A[N-1] = B[N-2]
    print(sum(A))

=======
Suggestion 3

def max_sum(a):
    sum = 0
    for i in range(len(a)):
        if i == 0:
            sum += a[i]
        else:
            sum += max(a[i-1], a[i])
    return sum

=======
Suggestion 4

def max_sum(n, b):
    a = [b[0]]
    for i in range(1, n-1):
        a.append(max(b[i], b[i-1]))
    a.append(b[n-2])
    return sum(a)

=======
Suggestion 5

def solve(n, b):
    a = [0] * n
    a[0] = b[0]
    a[-1] = b[-1]
    for i in range(1, n - 1):
        a[i] = min(b[i - 1], b[i])
    return sum(a)

=======
Suggestion 6

def main():
    n = int(input())
    b = list(map(int, input().split()))
    a = [0] * n
    a[0] = b[0]
    a[n-1] = b[n-2]
    for i in range(n-2):
        a[i+1] = min(b[i], b[i+1])
    print(sum(a))

=======
Suggestion 7

def max_sum():
    N = int(input())
    B = list(map(int, input().split()))
    A = [0]*N
    A[0] = B[0]
    A[N-1] = B[N-2]
    for i in range(1, N-1):
        A[i] = min(B[i-1], B[i])
    print(sum(A))

=======
Suggestion 8

def maxA(a, b):
    if a > b:
        return a
    else:
        return b

=======
Suggestion 9

def main():
    N = int(input())
    B = list(map(int, input().split()))
    A = [0] * N
    A[0] = B[0]
    A[N - 1] = B[N - 2]
    for i in range(1, N - 1):
        A[i] = min(B[i - 1], B[i])
    print(sum(A))

=======
Suggestion 10

def solve(n, b):
    a = [0] * n
    a[0] = b[0]
    for i in range(1, n-1):
        a[i] = max(b[i-1], b[i])
    a[n-1] = b[n-2]
    return sum(a)
