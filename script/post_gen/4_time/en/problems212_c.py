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
    min_diff = 10 ** 9 + 1
    while i < N and j < M:
        min_diff = min(min_diff, abs(A[i] - B[j]))
        if A[i] < B[j]:
            i += 1
        else:
            j += 1
    print(min_diff)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    i = 0
    j = 0
    ans = 10**9
    while i < n and j < m:
        ans = min(ans, abs(a[i]-b[j]))
        if a[i] < b[j]:
            i += 1
        else:
            j += 1

    print(ans)

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    i = 0
    j = 0
    min_diff = 1000000000
    while i < n and j < m:
        diff = abs(a[i] - b[j])
        if diff < min_diff:
            min_diff = diff
        if a[i] < b[j]:
            i += 1
        else:
            j += 1

    print(min_diff)

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    i = 0
    j = 0
    min_diff = 10**9
    while i < n and j < m:
        if a[i] == b[j]:
            min_diff = 0
            break
        elif a[i] < b[j]:
            min_diff = min(min_diff, b[j] - a[i])
            i += 1
        else:
            min_diff = min(min_diff, a[i] - b[j])
            j += 1

    print(min_diff)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    min_diff = 10**9
    for a in A:
        i = bisect.bisect_left(B, a)
        if i < M:
            min_diff = min(min_diff, abs(a - B[i]))
        if i > 0:
            min_diff = min(min_diff, abs(a - B[i-1]))

    print(min_diff)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    ans = 10**9
    i = 0
    j = 0
    while i < n and j < m:
        ans = min(ans, abs(a[i] - b[j]))
        if a[i] < b[j]:
            i += 1
        else:
            j += 1
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    result = 1000000000
    i = 0
    for b in B:
        while i < N and A[i] < b:
            i += 1
        if i == 0:
            result = min(result, abs(A[i] - b))
        elif i == N:
            result = min(result, abs(A[i - 1] - b))
        else:
            result = min(result, abs(A[i - 1] - b), abs(A[i] - b))
    print(result)

=======
Suggestion 8

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    ans = 10**9
    i = 0
    for j in range(m):
        while i < n - 1 and a[i] < b[j]:
            i += 1
        ans = min(ans, abs(a[i] - b[j]))
    print(ans)

=======
Suggestion 9

def solve(n,m,a,b):
    a.sort()
    b.sort()
    i = 0
    j = 0
    min_diff = 10**9
    while i < n and j < m:
        diff = abs(a[i]-b[j])
        if diff < min_diff:
            min_diff = diff
        if a[i] < b[j]:
            i += 1
        else:
            j += 1
    return min_diff

=======
Suggestion 10

def find_min_diff(A, B):
    A.sort()
    B.sort()
    min_diff = 10**9
    for a in A:
        for b in B:
            diff = abs(a-b)
            if diff < min_diff:
                min_diff = diff
            else:
                break
    return min_diff
