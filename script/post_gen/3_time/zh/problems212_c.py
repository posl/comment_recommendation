Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(n, m, a, b):
    a.sort()
    b.sort()
    i = 0
    j = 0
    ans = 0x7fffffff
    while i < n and j < m:
        ans = min(ans, abs(a[i] - b[j]))
        if a[i] < b[j]:
            i += 1
        else:
            j += 1
    return ans

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    j = 0
    ans = abs(a[0] - b[0])
    for i in range(n):
        while j < m - 1 and abs(a[i] - b[j + 1]) < abs(a[i] - b[j]):
            j += 1
        ans = min(ans, abs(a[i] - b[j]))
    print(ans)

=======
Suggestion 3

def min_diff(A,B):
    A.sort()
    B.sort()
    i = 0
    j = 0
    min_diff = 999999999
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            return 0
        elif A[i] > B[j]:
            min_diff = min(min_diff,A[i]-B[j])
            j += 1
        else:
            min_diff = min(min_diff,B[j]-A[i])
            i += 1
    return min_diff

=======
Suggestion 4

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    ans = 10**9
    i = 0
    for x in a:
        while i+1 < m and b[i+1] < x:
            i += 1
        ans = min(ans,abs(x-b[i]))
        if i+1 < m:
            ans = min(ans,abs(x-b[i+1]))
    print(ans)

=======
Suggestion 5

def get_min_diff(a, b):
    a = sorted(a)
    b = sorted(b)
    i = 0
    j = 0
    min_diff = 1000000000
    while i < len(a) and j < len(b):
        min_diff = min(min_diff, abs(a[i]-b[j]))
        if a[i] < b[j]:
            i += 1
        else:
            j += 1
    return min_diff

=======
Suggestion 6

def main():
    n,m = map(int, input().split())
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
Suggestion 7

def main():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort()
    b.sort()
    ans=10**9
    j=0
    for i in range(n):
        while j<m-1 and b[j+1]<=a[i]:
            j+=1
        ans=min(ans,abs(a[i]-b[j]))
        if j<m-1:
            ans=min(ans,abs(a[i]-b[j+1]))
    print(ans)

=======
Suggestion 8

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    ans = 10**9
    j = 0
    for i in range(n):
        while j < m - 1 and abs(a[i] - b[j]) > abs(a[i] - b[j+1]):
            j += 1
        ans = min(ans, abs(a[i] - b[j]))
    print(ans)

=======
Suggestion 9

def min_difference(a, b):
    a.sort()
    b.sort()
    i = 0
    j = 0
    min_diff = abs(a[0] - b[0])
    while i < len(a) and j < len(b):
        diff = abs(a[i] - b[j])
        if diff < min_diff:
            min_diff = diff
        if a[i] < b[j]:
            i += 1
        else:
            j += 1
    return min_diff

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(min_difference(a, b))

=======
Suggestion 10

def solve():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    ans = 1 << 30
    j = 0
    for i in range(n):
        while j + 1 < m and B[j + 1] <= A[i]:
            j += 1
        ans = min(ans, abs(A[i] - B[j]))
        if j + 1 < m:
            ans = min(ans, abs(A[i] - B[j + 1]))
    print(ans)

solve()
