Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    i = 0
    j = 0
    ans = 10**9
    while i < N and j < M:
        ans = min(ans, abs(A[i] - B[j]))
        if A[i] < B[j]:
            i += 1
        else:
            j += 1
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    i = 0
    j = 0
    min_diff = abs(A[0] - B[0])
    while i < N and j < M:
        diff = abs(A[i] - B[j])
        if diff < min_diff:
            min_diff = diff
        if A[i] < B[j]:
            i += 1
        else:
            j += 1
    print(min_diff)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    i = 0
    j = 0
    ans = 10**9
    while i < N and j < M:
        ans = min(abs(A[i]-B[j]), ans)
        if A[i] < B[j]:
            i += 1
        else:
            j += 1
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    ans = float('inf')
    i = j = 0
    while i < N and j < M:
        ans = min(ans, abs(A[i] - B[j]))
        if A[i] < B[j]:
            i += 1
        else:
            j += 1
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A = sorted(A)
    B = sorted(B)
    ans = 10**9
    i = 0
    j = 0
    while i < N and j < M:
        ans = min(ans, abs(A[i] - B[j]))
        if A[i] > B[j]:
            j += 1
        else:
            i += 1
    print(ans)

=======
Suggestion 6

def main():
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    i = 0
    j = 0
    ans = 10**9
    while i < N and j < M:
        ans = min(ans, abs(A[i] - B[j]))
        if A[i] > B[j]:
            j += 1
        else:
            i += 1
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 10**9
    for a in A:
        for b in B:
            ans = min(ans, abs(a-b))
    print(ans)

=======
Suggestion 8

def binarySearch(a, x):
    left = 0
    right = len(a)
    while left < right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
ans = 10 ** 9 + 1
for i in range(n):
    j = binarySearch(b, a[i])
    if j < m:
        ans = min(ans, abs(a[i] - b[j]))
    if j > 0:
        ans = min(ans, abs(a[i] - b[j - 1]))
print(ans)

=======
Suggestion 9

def main():
    # read input
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # sort A and B
    A.sort()
    B.sort()
    # find minimum difference
    i = 0
    j = 0
    min_diff = abs(A[0] - B[0])
    while i < N and j < M:
        min_diff = min(min_diff, abs(A[i] - B[j]))
        if A[i] < B[j]:
            i += 1
        else:
            j += 1
    print(min_diff)

=======
Suggestion 10

def min_diff(a, b):
    a.sort()
    b.sort()

    i = 0
    j = 0
    min_diff = 10**9
    while i < len(a) and j < len(b):
        if abs(a[i] - b[j]) < min_diff:
            min_diff = abs(a[i] - b[j])
        if a[i] < b[j]:
            i += 1
        else:
            j += 1
    return min_diff
