Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[1])

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a)
    print(a.index(b[1])+1)

=======
Suggestion 3

def main():
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[1])

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))

    min1 = min(A)
    min2 = min(filter(lambda x: x != min1, A))

    print(A.index(min2) + 1)

=======
Suggestion 5

def main():
    n = int(input())
    scores = list(map(int, input().split()))
    scores.sort()
    print(scores[1])

=======
Suggestion 6

def rank2(arr):
    arr = sorted(arr)
    return arr[1]

=======
Suggestion 7

def main():
    #N = int(input())
    #A = list(map(int, input().split()))
    N = 6
    A = [1, 123, 12345, 12, 1234, 123456]
    #N = 5
    #A = [3, 1, 4, 15, 9]
    A.sort()
    print(A[1])

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = sorted(A)
    print(A.index(B[1])+1)
