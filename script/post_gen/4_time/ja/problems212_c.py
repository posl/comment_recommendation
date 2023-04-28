Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    i = 0
    j = 0
    min = 1000000001

    while i < n and j < m:
        if a[i] <= b[j]:
            if min > b[j] - a[i]:
                min = b[j] - a[i]
            i += 1
        else:
            if min > a[i] - b[j]:
                min = a[i] - b[j]
            j += 1

    print(min)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    ans = 10**9
    i = 0
    for j in range(m):
        while i < n and a[i] < b[j]:
            i += 1
        if i < n:
            ans = min(ans, abs(a[i]-b[j]))
        if i > 0:
            ans = min(ans, abs(a[i-1]-b[j]))
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    min_diff = 10**9
    i = 0
    j = 0

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
Suggestion 4

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
        ans = min(ans, abs(a[i]-b[j]))
        if a[i] < b[j]:
            i += 1
        else:
            j += 1
    print(ans)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    min_diff = 10**9
    i = 0
    j = 0

    while i < n and j < m:
        min_diff = min(min_diff, abs(a[i] - b[j]))
        if a[i] < b[j]:
            i += 1
        else:
            j += 1

    print(min_diff)

=======
Suggestion 6

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    ans = 10**9
    for i in range(N):
        for j in range(M):
            ans = min(ans,abs(A[i] - B[j]))
    print(ans)

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
        while l<=r:
            mid = (l+r)//2
            if b[mid] < a[i]:
                l = mid+1
            else:
                r = mid-1
        if l < m:
            ans = min(ans,abs(a[i]-b[l]))
        if l > 0:
            ans = min(ans,abs(a[i]-b[l-1]))
    print(ans)

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()
    min_diff = 10**9
    for i in range(n):
        diff = abs(a[i] - b[0])
        if diff < min_diff:
            min_diff = diff
        for j in range(m):
            diff = abs(a[i] - b[j])
            if diff < min_diff:
                min_diff = diff
            else:
                break
    print(min_diff)

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    min = 10**9
    for i in range(n):
        for j in range(m):
            if min > abs(a[i] - b[j]):
                min = abs(a[i] - b[j])
    print(min)

=======
Suggestion 10

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    a.sort()
    b.sort()
    a_index = 0
    b_index = 0
    min_diff = 10**9+1
    while a_index < n and b_index < m:
        diff = abs(a[a_index] - b[b_index])
        if diff < min_diff:
            min_diff = diff
        if a[a_index] < b[b_index]:
            a_index += 1
        else:
            b_index += 1

    print(min_diff)
