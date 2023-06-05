Synthesizing 10/10 solutions

=======
Suggestion 1

def exchange(perm):
    for i in range(len(perm)):
        if perm[i] > perm[i+1]:
            return i
    return -1

=======
Suggestion 2

def get_next_permutation(a):
    n = len(a)
    i = n - 1
    while a[i - 1] >= a[i]:
        i -= 1
    j = n - 1
    while j >= i and a[j] <= a[i - 1]:
        j -= 1
    a[i - 1], a[j] = a[j], a[i - 1]
    a[i:] = a[n - 1: i - 1: -1]
    return a

n = int(input())
p = list(map(int, input().split()))
q = get_next_permutation(p)
print(*q)

=======
Suggestion 3

def main():
    n = int(input())
    p = list(map(int,input().split()))
    k = 1
    for i in range(n):
        for j in range(i+1,n):
            if p[i]>p[j]:
                k += 1
    q = [0]*n
    q[0] = k
    for i in range(1,n):
        k = 1
        for j in range(i+1,n):
            if p[i-1]>p[j]:
                k += 1
        q[i] = k
    print(" ".join(map(str,q)))

=======
Suggestion 4

def problems276_c():
    pass

=======
Suggestion 5

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

=======
Suggestion 6

def get_next_permutation(arr):
    n = len(arr)
    for i in range(n - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            break
    else:
        return arr[::-1]

    for j in range(n - 1, i, -1):
        if arr[j] > arr[i]:
            break

    arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1:] = arr[i + 1:][::-1]

    return arr

n = int(input())
p = list(map(int, input().split()))

p = get_next_permutation(p)
print(*p)

=======
Suggestion 7

def find_min_index(nums):
    min_index = 0
    min_num = nums[0]
    for i in range(1,len(nums)):
        if nums[i] < min_num:
            min_num = nums[i]
            min_index = i
    return min_index

=======
Suggestion 8

def main():
    n = int(input())
    p = [int(i) for i in input().split()]
    q = [0] * n
    for i in range(n):
        q[p[i]-1] = i+1
    print(' '.join([str(i) for i in q]))

=======
Suggestion 9

def get_input():
    n = int(input())
    p = list(map(int, input().split()))
    return n, p

=======
Suggestion 10

def main():
    N = int(input())
    P = list(map(int, input().split()))

    Q = [0] * N
    for i in range(N):
        Q[P[i]-1] = i+1
    print(*Q)
