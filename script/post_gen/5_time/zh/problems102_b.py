Synthesizing 10/10 solutions

=======
Suggestion 1

def get_max_abs_diff(a_list):
    a_list.sort()
    return a_list[-1] - a_list[0]

=======
Suggestion 2

def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    a_list.sort()
    print(a_list[-1] - a_list[0])

=======
Suggestion 3

def max_difference():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    return a[n-1] - a[0]

print(max_difference())

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    max = 0
    for i in range(n):
        for j in range(i+1, n):
            if abs(a[i]-a[j]) > max:
                max = abs(a[i]-a[j])
    print(max)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_a = max(a)
    min_a = min(a)
    print(max_a - min_a)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(max(A) - min(A))

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))

    max_num = 0
    for i in range(N):
        for j in range(i+1, N):
            if max_num < abs(A[i] - A[j]):
                max_num = abs(A[i] - A[j])

    print(max_num)

=======
Suggestion 8

def max_abs_diff(n, a):
    max_diff = 0
    for i in range(n):
        for j in range(i+1, n):
            diff = abs(a[i] - a[j])
            if diff > max_diff:
                max_diff = diff
    return max_diff

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    max_num = max(A)
    min_num = min(A)
    print(max_num - min_num)

=======
Suggestion 10

def get_max_diff(arr):
    max = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            diff = abs(arr[i]-arr[j])
            if diff > max:
                max = diff
    return max
