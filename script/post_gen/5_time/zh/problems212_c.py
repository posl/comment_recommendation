Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    i,j = 0,0
    min = 1000000000
    while i < n and j < m:
        if A[i] < B[j]:
            if B[j] - A[i] < min:
                min = B[j] - A[i]
            i += 1
        else:
            if A[i] - B[j] < min:
                min = A[i] - B[j]
            j += 1
    print(min)

=======
Suggestion 2

def solution():
    pass

=======
Suggestion 3

def min_diff(a, b):
    a.sort()
    b.sort()
    min_d = 10 ** 9
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        min_d = min(min_d, abs(a[i] - b[j]))
        if a[i] < b[j]:
            i += 1
        else:
            j += 1
    return min_d

=======
Suggestion 4

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    ans = 10**9
    i = 0
    for x in b:
        while i < n and a[i] <= x:
            i += 1
        if i > 0:
            ans = min(ans, abs(x-a[i-1]))
        if i < n:
            ans = min(ans, abs(a[i]-x))
    print(ans)

solve()

=======
Suggestion 5

def main():
    n = int(input().split()[0])
    a = list(map(int, input().split()))
    m = int(input().split()[0])
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    i = 0
    j = 0
    ans = 10 ** 9
    while i < n and j < m:
        ans = min(ans, abs(a[i] - b[j]))
        if a[i] > b[j]:
            j += 1
        else:
            i += 1
    print(ans)

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    a = sorted(list(map(int,input().split())))
    b = sorted(list(map(int,input().split())))
    ans = 2*10**9
    i = 0
    for x in b:
        while i < n and a[i] <= x:
            i += 1
        if i > 0:
            ans = min(ans,abs(x-a[i-1]))
        if i < n:
            ans = min(ans,abs(x-a[i]))
    print(ans)

=======
Suggestion 7

def solve():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    ans = 10 ** 9 + 1
    for a in A:
        ok = -1
        ng = M
        while ng - ok > 1:
            mid = (ok + ng) // 2
            if B[mid] >= a:
                ng = mid
            else:
                ok = mid
        ans = min(ans,abs(a - B[ng]))
        if ng + 1 < M:
            ans = min(ans,abs(a - B[ng + 1]))
    print(ans)

solve()

=======
Suggestion 8

def getMinDiff(a,b):
    a.sort()
    b.sort()
    min_diff = abs(a[0] - b[0])
    for i in range(len(a)):
        for j in range(len(b)):
            if abs(a[i] - b[j]) < min_diff:
                min_diff = abs(a[i] - b[j])
    return min_diff

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    ans = 10 ** 9
    j = 0
    for i in range(n):
        while j < m - 1 and b[j + 1] <= a[i]:
            j += 1
        ans = min(ans, abs(a[i] - b[j]))
        if j < m - 1:
            ans = min(ans, abs(a[i] - b[j + 1]))
    print(ans)

=======
Suggestion 10

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    ai = 0
    bi = 0
    ans = 10**9

    while ai < n and bi < m:
        ans = min(ans, abs(a[ai] - b[bi]))
        if a[ai] < b[bi]:
            ai += 1
        else:
            bi += 1
    
    print(ans)
