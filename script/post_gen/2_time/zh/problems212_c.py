Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    i, j = 0, 0
    ans = 1000000000000000000
    while i < N and j < M:
        ans = min(ans, abs(A[i] - B[j]))
        if A[i] < B[j]:
            i += 1
        else:
            j += 1
    print(ans)

=======
Suggestion 2

def min_dif(a, b):
    a.sort()
    b.sort()
    i = 0
    j = 0
    ans = abs(a[i] - b[j])
    while i < len(a) and j < len(b):
        if abs(a[i] - b[j]) < ans:
            ans = abs(a[i] - b[j])
        if a[i] < b[j]:
            i += 1
        else:
            j += 1
    return ans

=======
Suggestion 3

def min_diff(a, b):
    a.sort()
    b.sort()
    i = 0
    j = 0
    min_diff = abs(a[0] - b[0])
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            return 0
        elif a[i] < b[j]:
            min_diff = min(min_diff, b[j] - a[i])
            i += 1
        else:
            min_diff = min(min_diff, a[i] - b[j])
            j += 1
    return min_diff

=======
Suggestion 4

def min_diff(arr1, arr2):
    arr1.sort()
    arr2.sort()
    i, j = 0, 0
    min_diff = abs(arr1[i] - arr2[j])
    while i < len(arr1) and j < len(arr2):
        min_diff = min(min_diff, abs(arr1[i] - arr2[j]))
        if arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    return min_diff

=======
Suggestion 5

def getMinDiff(A,B):
    A.sort()
    B.sort()
    minDiff = abs(A[0]-B[0])
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        minDiff = min(minDiff,abs(A[i]-B[j]))
        if A[i] < B[j]:
            i += 1
        else:
            j += 1
    return minDiff

=======
Suggestion 6

def read_ints():
    return [int(x) for x in input().split()]

n,m = read_ints()
a = read_ints()
b = read_ints()
a.sort()
b.sort()
ans = 10**9
j = 0
for i in range(n):
    while j < m and b[j] <= a[i]:
        ans = min(ans, a[i] - b[j])
        j += 1
    if j < m:
        ans = min(ans, b[j] - a[i])
print(ans)

=======
Suggestion 7

def min_diff(A, B):
    A.sort()
    B.sort()
    i, j = 0, 0
    min_diff = abs(A[0] - B[0])
    while i < len(A) and j < len(B):
        min_diff = min(min_diff, abs(A[i] - B[j]))
        if A[i] < B[j]:
            i += 1
        else:
            j += 1
    return min_diff

=======
Suggestion 8

def findMinDiff(A, B, n, m):
    A.sort()
    B.sort()
    a = 0
    b = 0
    result = 999999999999
    while(a<n and b<m):
        if(abs(A[a]-B[b])<result):
            result = abs(A[a]-B[b])
        if(A[a]>B[b]):
            b+=1
        else:
            a+=1
    return result

=======
Suggestion 9

def main():
    n,m = map(int, input().split())
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
Suggestion 10

def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    ans = 10**9
    i = 0
    for x in a:
        while i < m and b[i] <= x:
            i += 1
        if i != 0:
            ans = min(ans, x - b[i-1])
        if i != m:
            ans = min(ans, b[i] - x)
    print(ans)

main()
