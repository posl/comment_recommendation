Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]

    a.sort()
    for i in range(q):
        print(n - bisect.bisect_left(a, x[i]))

=======
Suggestion 2

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(q):
        x = int(input())
        idx = binary_search(a, x)
        if idx == -1:
            print(n)
        else:
            print(n - idx)

=======
Suggestion 3

def binarySearch (arr, l, r, x): 
    if r >= l: 
        mid = int(l + (r - l)/2)
        if arr[mid] == x: 
            return mid 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
        else: 
            return binarySearch(arr, mid+1, r, x) 
    else: 
        return -1

=======
Suggestion 4

def main():
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))
    x = [int(input()) for i in range(Q)]
    A.sort()
    for i in range(Q):
        count = 0
        for j in range(N):
            if A[j] >= x[i]:
                count += 1
        print(count)

=======
Suggestion 5

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    a.sort()
    for i in range(q):
        print(n - bisect.bisect_left(a, x[i]))

main()

=======
Suggestion 6

def count_higher_than_x(a, x):
    a.sort()
    count = 0
    for i in range(len(a)):
        if a[i] >= x:
            count += 1
    return count

=======
Suggestion 7

def main():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    x = []
    for i in range(q):
        x.append(int(input()))
    a.sort()
    for i in range(q):
        l = 0
        r = n-1
        while l<r:
            m = (l+r)//2
            if a[m]<x[i]:
                l = m+1
            else:
                r = m
        if a[l]<x[i]:
            print(0)
        else:
            print(n-l)

=======
Suggestion 8

def solve():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = []
    for i in range(q):
        x.append(int(input()))
    a.sort()
    for i in range(q):
        cnt = 0
        for j in range(n):
            if x[i] <= a[j]:
                cnt += 1
        print(cnt)


solve()

=======
Suggestion 9

def main():
    n,q = map(int, input().split())
    a = list(map(int, input().split()))
    x = []
    for i in range(q):
        x.append(int(input()))
    a.sort()
    for i in range(q):
        j = 0
        while j < n:
            if a[j] >= x[i]:
                break
            j += 1
        print(n - j)

=======
Suggestion 10

def binary_search(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

n, q = map(int, input().split())
a = list(map(int, input().split()))
x = [int(input()) for _ in range(q)]
a.sort()
for i in range(q):
    print(n - binary_search(a, x[i]))
