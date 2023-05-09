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
    min = 1000000000
    while i < N and j < M:
        if abs(A[i] - B[j]) < min:
            min = abs(A[i] - B[j])
        if A[i] < B[j]:
            i += 1
        else:
            j += 1

    print(min)

=======
Suggestion 2

def main():
    N, M = map(int, input().split(" "))
    A = list(map(int, input().split(" ")))
    B = list(map(int, input().split(" ")))
    A.sort()
    B.sort()
    i = 0
    j = 0
    min_diff = 10**9
    while i < N and j < M:
        diff = abs(A[i]-B[j])
        min_diff = min(min_diff, diff)
        if A[i] < B[j]:
            i += 1
        else:
            j += 1
    print(min_diff)

=======
Suggestion 3

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
Suggestion 4

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    min_diff = 10 ** 9 + 1
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
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    ans = 10**9
    j = 0
    for i in range(N):
        while j < M-1 and abs(A[i]-B[j]) >= abs(A[i]-B[j+1]):
            j += 1
        ans = min(ans, abs(A[i]-B[j]))
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    min = 10**9 + 1

    i = 0
    j = 0

    while i < N and j < M:
        if abs(A[i] - B[j]) < min:
            min = abs(A[i] - B[j])

        if A[i] < B[j]:
            i += 1
        else:
            j += 1

    print(min)

main()

=======
Suggestion 7

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    ans = 10**9
    j = 0
    for i in range(n):
        while j < m-1 and b[j+1] <= a[i]:
            j += 1
        ans = min(ans, abs(a[i] - b[j]))
    print(ans)

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    min_diff = None
    for i in range(n):
        for j in range(m):
            diff = abs(a[i] - b[j])
            if min_diff is None or diff < min_diff:
                min_diff = diff

    print(min_diff)

=======
Suggestion 9

def solve():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    ans = 10**9
    i,j = 0,0
    while i < N and j < M:
        ans = min(ans,abs(A[i]-B[j]))
        if A[i] < B[j]:
            i += 1
        else:
            j += 1
    print(ans)
solve()

=======
Suggestion 10

def minimum_difference():
    #input
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    #sort
    a.sort()
    b.sort()
    #initialize
    min_diff = 10 ** 9 + 1
    #search
    i = 0
    j = 0
    while i < n and j < m:
        diff = abs(a[i] - b[j])
        if min_diff > diff:
            min_diff = diff
        if a[i] < b[j]:
            i += 1
        else:
            j += 1
    #output
    print(min_diff)
