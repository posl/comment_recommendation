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
    a.sort()
    print(a[1])

main()

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[1])

main()

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(a[1])

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [(a, i) for i, a in enumerate(A)]
    A = sorted(A, key=lambda x: x[0])
    print(A[1][1] + 1)

main()

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = sorted(A)
    print(A[1])
