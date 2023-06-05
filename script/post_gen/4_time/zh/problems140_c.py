Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def sum_max(a):
    sum = 0
    for i in a:
        sum += i
    return sum

=======
Suggestion 2

def maxsum(A):
    if len(A) == 1:
        return A[0]
    elif len(A) == 2:
        return max(A)
    else:
        maxA = max(A)
        i = A.index(maxA)
        if i == 0:
            return maxA + maxsum(A[i+1:])
        elif i == len(A)-1:
            return maxA + maxsum(A[:i])
        else:
            return maxA + max(maxsum(A[:i]), maxsum(A[i+1:]))

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

def get_max_sum(arr):
    n = len(arr)
    if n == 2:
        return arr[0] + arr[1]
    sum = arr[0] + arr[1]
    for i in range(1, n-1):
        if arr[i] > arr[i-1]:
            sum += arr[i]
        else:
            sum += arr[i-1]
    sum += arr[-1]
    return sum

=======
Suggestion 5

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
Suggestion 6

def max_sum(n, b):
    a = [0 for i in range(n)]
    a[0] = b[0]
    a[-1] = b[-1]
    for i in range(1, n-1):
        if b[i] <= b[i-1]:
            a[i] = b[i]
        else:
            a[i] = b[i-1]
    return sum(a)

=======
Suggestion 7

def solve(n, b):
    a = []
    a.append(b[0])
    for i in range(1, n-1):
        a.append(max(b[i], b[i-1]))
    a.append(b[n-2])
    return sum(a)

=======
Suggestion 8

def main():
    n = int(input())
    b = list(map(int, input().split()))
    a = [0] * n
    a[0] = b[0]
    a[-1] = b[-1]
    for i in range(1, n - 1):
        a[i] = min(b[i - 1], b[i])
    print(sum(a))

=======
Suggestion 9

def solve(n, b):
    a = [0] * n
    a[0] = b[0]
    for i in range(1, n):
        a[i] = min(b[i-1], b[i])
    return sum(a)
