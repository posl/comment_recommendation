Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    for i in range(q):
        count = 0
        for j in range(n):
            if a[j] >= x[i]:
                count += 1
        print(count)

=======
Suggestion 2

def binary_search(x, array, left, right):
    if left == right:
        return left
    if left + 1 == right:
        if array[left] >= x:
            return left
        else:
            return right
    middle = (left + right) // 2
    if array[middle] >= x:
        return binary_search(x, array, left, middle)
    else:
        return binary_search(x, array, middle, right)

=======
Suggestion 3

def binary_search(a, x):
    """二分查找"""
    n = len(a)
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

n, q = map(int, input().split())
a = list(map(int, input().split()))
a = sorted(a)
for _ in range(q):
    x = int(input())
    print(binary_search(a, x) + 1)

=======
Suggestion 4

def main():
    n,q = map(int, input().split())
    A = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]

    for i in range(q):
        count = 0
        for j in range(n):
            if A[j] >= x[i]:
                count += 1
        print(count)

=======
Suggestion 5

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    x = [int(input()) for _ in range(q)]
    for i in range(q):
        print(n - (len(a) - bisect.bisect_left(a, x[i])))

=======
Suggestion 6

def main():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    for i in range(q):
        x = int(input())
        cnt = 0
        for j in range(n):
            if a[j] >= x:
                cnt += 1
        print(cnt)

=======
Suggestion 7

def binary_search(array, x):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == x:
            return mid
        elif array[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
    return left

n, q = map(int, input().split())
a = list(map(int, input().split()))
x = [int(input()) for _ in range(q)]
a.sort()

for i in range(q):
    print(n - binary_search(a, x[i]))

=======
Suggestion 8

def main():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    x = [int(input()) for _ in range(q)]
    a.sort()
    for i in x:
        print(n - (a.index(i) if i in a else len(a) - 1 - a[::-1].index(i) + 1))

=======
Suggestion 9

def solve():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(Q):
        x = int(input())
        low = 0
        high = N - 1
        while low < high:
            mid = (low + high) // 2
            if A[mid] >= x:
                high = mid
            else:
                low = mid + 1
        if A[low] >= x:
            print(N - low)
        else:
            print(N - low - 1)

=======
Suggestion 10

def binary_search(a, x, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if a[mid] == x:
        return mid
    elif a[mid] > x:
        return binary_search(a, x, low, mid - 1)
    else:
        return binary_search(a, x, mid + 1, high)
