Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
	n, q = map(int, input().split())
	student = list(map(int, input().split()))
	student.sort()
	for i in range(q):
		x = int(input())
		# 二分查找
		low = 0
		high = n
		while low < high:
			mid = (low + high) // 2
			if student[mid] >= x:
				high = mid
			else:
				low = mid + 1
		print(n - low)

=======
Suggestion 2

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = int((high + low) / 2)
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return mid

=======
Suggestion 3

def binary_search(l, r, x, a):
    if l == r:
        return l
    m = (l + r) // 2
    if a[m] >= x:
        return binary_search(l, m, x, a)
    else:
        return binary_search(m + 1, r, x, a)

=======
Suggestion 4

def binary_search(x, a):
    left = 0
    right = len(a)
    while left < right:
        mid = (left + right) // 2
        if x == a[mid]:
            return mid
        elif x > a[mid]:
            left = mid + 1
        else:
            right = mid
    return left

=======
Suggestion 5

def main():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    x = []
    for i in range(q):
        x.append(int(input()))
    a.sort()
    for i in range(q):
        count = 0
        for j in range(n):
            if x[i] <= a[j]:
                count += 1
        print(count)

=======
Suggestion 6

def solve(n, q, a, x):
    a.sort()
    for i in range(q):
        print(n - bisect.bisect_left(a, x[i]))

=======
Suggestion 7

def main():
    pass

=======
Suggestion 8

def binary_search(A, x):
    left = 0
    right = len(A) - 1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == x:
            return mid
        elif A[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return left

=======
Suggestion 9

def main():
    n,q = map(int, input().split())
    A = list(map(int, input().split()))
    x = []
    for i in range(q):
        x.append(int(input()))
    A.sort()
    for i in range(q):
        num = 0
        for j in range(n):
            if x[i] <= A[j]:
                num += 1
        print(num)

=======
Suggestion 10

def solve(n, q, a, x):
    a.sort()
    for i in range(q):
        print(binary_search(a, x[i]))
