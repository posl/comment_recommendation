Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    min_diff = 10**9
    i = 0
    j = 0
    while i<n and j<m:
        min_diff = min(min_diff,abs(A[i]-B[j]))
        if A[i]>B[j]:
            j += 1
        else:
            i += 1
    print(min_diff)

=======
Suggestion 2

def minDiff(a, b):
    a.sort()
    b.sort()
    i, j = 0, 0
    minDiff = 2 * 10**9
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            minDiff = min(minDiff, b[j] - a[i])
            i += 1
        elif a[i] > b[j]:
            minDiff = min(minDiff, a[i] - b[j])
            j += 1
        else:
            minDiff = 0
            break
    return minDiff

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(minDiff(a, b))

=======
Suggestion 3

def main():
    n,m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    min_diff = 1000000000
    for i in range(n):
        diff = abs(A[i] - B[0])
        if diff < min_diff:
            min_diff = diff
        for j in range(m):
            diff = abs(A[i] - B[j])
            if diff < min_diff:
                min_diff = diff
            else:
                break

    print(min_diff)

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    ans = float('inf')
    i = 0
    for x in a:
        while i < m and b[i] < x:
            i += 1
        if i < m:
            ans = min(ans, b[i] - x)
        if i > 0:
            ans = min(ans, x - b[i-1])
    print(ans)

=======
Suggestion 5

def minDiff(A, B):
    A.sort()
    B.sort()
    a, b = 0, 0
    min_diff = abs(A[0] - B[0])
    while a < len(A) and b < len(B):
        min_diff = min(min_diff, abs(A[a] - B[b]))
        if A[a] > B[b]:
            b += 1
        else:
            a += 1
    return min_diff

=======
Suggestion 6

def min_diff(a, b):
    a.sort()
    b.sort()
    min_diff = float('inf')
    i, j = 0, 0
    while i < len(a) and j < len(b):
        min_diff = min(min_diff, abs(a[i] - b[j]))
        if a[i] < b[j]:
            i += 1
        else:
            j += 1
    return min_diff

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    ans = 10**9
    for i in range(n):
        l = 0
        r = m-1
        while l<r:
            mid = (l+r)//2
            if b[mid]<a[i]:
                l = mid+1
            else:
                r = mid
        if l>0:
            ans = min(ans,abs(a[i]-b[l-1]))
        ans = min(ans,abs(a[i]-b[l]))
        if l<m-1:
            ans = min(ans,abs(a[i]-b[l+1]))
    print(ans)

=======
Suggestion 8

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    i = 0
    j = 0

    min_diff = 2 * 10 ** 9

    while i < n and j < m:
        min_diff = min(min_diff, abs(a[i] - b[j]))

        if a[i] < b[j]:
            i += 1
        else:
            j += 1

    print(min_diff)

solve()

=======
Suggestion 9

def min_diff(a, b):
    a.sort()
    b.sort()
    a_len = len(a)
    b_len = len(b)
    i = 0
    j = 0
    min_diff = 2 ** 32
    while i < a_len and j < b_len:
        if a[i] == b[j]:
            return 0
        elif a[i] < b[j]:
            if j > 0:
                min_diff = min(min_diff, b[j] - a[i], a[i] - b[j - 1])
            else:
                min_diff = min(min_diff, b[j] - a[i])
            i += 1
        else:
            if i > 0:
                min_diff = min(min_diff, a[i] - b[j], b[j] - a[i - 1])
            else:
                min_diff = min(min_diff, a[i] - b[j])
            j += 1
    return min_diff

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()
    i = 0
    j = 0
    ans = 1e9
    while i < n and j < m:
        ans = min(ans, abs(a[i] - b[j]))
        if a[i] < b[j]:
            i += 1
        else:
            j += 1
    print(ans)
