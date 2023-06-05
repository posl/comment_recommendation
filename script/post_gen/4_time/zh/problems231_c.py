Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    for i in range(q):
        x = int(input())
        if x < a[0]:
            print(0)
        elif x >= a[-1]:
            print(n)
        else:
            l = 0
            r = n-1
            while l < r:
                mid = (l+r)//2
                if a[mid] < x:
                    l = mid + 1
                else:
                    r = mid
            print(n-r)

=======
Suggestion 2

def binarySearch(arr, l, r, x):
    if (r >= l):
        mid = int(l + (r - l) / 2)
        if (arr[mid] == x):
            return mid
        elif (arr[mid] > x):
            return binarySearch(arr, l, mid - 1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return -1

=======
Suggestion 3

def binary_search(A, key):
    left = 0
    right = len(A)
    while left < right:
        mid = (left + right) // 2
        if A[mid] == key:
            return mid
        elif key < A[mid]:
            right = mid
        else:
            left = mid + 1
    return right

=======
Suggestion 4

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    a.sort()
    for i in range(q):
        j = 0
        while a[j] < x[i]:
            j += 1
        print(n - j)

=======
Suggestion 5

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]

    a.sort()
    for i in range(q):
        for j in range(n):
            if x[i] <= a[j]:
                print(n - j)
                break

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    x = []
    for i in range(Q):
        x.append(int(input()))
    A.sort()
    for i in range(Q):
        count = 0
        for j in range(N):
            if A[j] >= x[i]:
                count += 1
        print(count)
    return 0

=======
Suggestion 7

def main():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    x = [int(input()) for _ in range(q)]
    a.sort()
    for i in range(q):
        j = 0
        while j < n and a[j] < x[i]:
            j += 1
        print(n-j)

=======
Suggestion 8

def main():
    n,q=map(int,input().split())
    A=list(map(int,input().split()))
    x=[int(input()) for _ in range(q)]
    A.sort()
    for i in range(q):
        print(n - len([a for a in A if a < x[i]]))

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
        ans = 0
        for j in range(n):
            if a[j] >= x[i]:
                ans += 1
        print(ans)

=======
Suggestion 10

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = []
    for i in range(q):
        x.append(int(input()))
    a.sort()
    for i in range(q):
        num = 0
        for j in range(n):
            if a[j] >= x[i]:
                num = n - j
                break
        print(num)
