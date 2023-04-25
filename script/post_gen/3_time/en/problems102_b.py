Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    maxA = max(A)
    minA = min(A)
    print(maxA - minA)

main()

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(max(A) - min(A))

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[-1] - A[0])

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[N-1]-A[0])

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(a[n-1]-a[0])

=======
Suggestion 6

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    print(max(a) - min(a))

=======
Suggestion 7

def max_diff(list):
    max_diff = 0
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            diff = abs(list[i] - list[j])
            if diff > max_diff:
                max_diff = diff
    return max_diff

=======
Suggestion 8

def max_diff(N, A):
    diff = 0
    for i in range(N):
        for j in range(i+1, N):
            if abs(A[i] - A[j]) > diff:
                diff = abs(A[i] - A[j])
    return diff
