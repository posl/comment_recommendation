Synthesizing 9/10 solutions

=======
Suggestion 1

def binary_search(a, n, key):
    left = 0
    right = n
    while left < right:
        mid = (left + right) // 2
        if a[mid] == key:
            return mid
        elif key < a[mid]:
            right = mid
        else:
            left = mid + 1
    return -1

n, q = map(int, input().split())
a = list(map(int, input().split()))
x = [int(input()) for _ in range(q)]
a.sort()
for i in x:
    print(binary_search(a, n, i) + 1)

=======
Suggestion 2

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    a.sort()
    for i in range(q):
        print(n - binary_search(a, x[i]) - 1)

=======
Suggestion 3

def binary_search(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right)//2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return right

=======
Suggestion 4

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
Suggestion 5

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    a.sort()
    for i in range(q):
        j = 0
        while j < n:
            if x[i] <= a[j]:
                print(n-j)
                break
            j += 1

=======
Suggestion 6

def main():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    x = [int(input()) for _ in range(q)]
    for i in range(q):
        print(n - binary_search(a,x[i]) + 1)

=======
Suggestion 7

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    a.sort()
    for i in range(q):
        print(n - bisect.bisect_left(a, x[i]))

=======
Suggestion 8

def main():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    x = [int(input()) for i in range(q)]
    a.sort()
    for i in range(q):
        if x[i] < a[0]:
            print(n)
        elif x[i] > a[n-1]:
            print(0)
        else:
            left = 0
            right = n-1
            while left < right:
                mid = (left+right)//2
                if a[mid] < x[i]:
                    left = mid+1
                else:
                    right = mid
            print(n-left)

=======
Suggestion 9

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(q):
        x = int(input())
        print(n - binary_search(a, x))
