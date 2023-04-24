Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(max(A) - min(A))

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(max(a) - min(a))

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    min = A[0]
    max = A[0]
    for i in range(1, N):
        if A[i] < min:
            min = A[i]
        elif A[i] > max:
            max = A[i]
    print(max - min)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(a[-1]-a[0])

=======
Suggestion 5

def main():
    #N = int(input())
    #A = list(map(int, input().split()))
    N = 5
    A = [1, 1, 1, 1, 1]
    A.sort()
    print(A)
    print(A[N-1]-A[0])
    return

=======
Suggestion 6

def maximum_absolute_difference_of_two_elements(array):
    array.sort()
    return array[-1] - array[0]
