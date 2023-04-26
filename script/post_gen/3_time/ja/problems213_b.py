Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_sorted = sorted(A)
    print(A.index(A_sorted[1]) + 1)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = sorted(A)
    print(A.index(B[1])+1)

=======
Suggestion 3

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A_sorted = sorted(A)
    print(A.index(A_sorted[1]) + 1)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[1])

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)
    print(a[1])

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = sorted(A)
    print(A[1])

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    min_score = min(A)
    A.remove(min_score)
    print(A.index(min(A)) + 2)

=======
Suggestion 8

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[1])

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()

    print(A[1])

main()
