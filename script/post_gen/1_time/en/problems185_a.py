Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a1, a2, a3, a4 = map(int, input().split())
    print(min(a1, a2, a3, a4))

=======
Suggestion 2

def solve():
    A = list(map(int, input().split()))
    print(min(A[0], A[2], A[3], A[1]//2))

=======
Suggestion 3

def main():
    A = list(map(int, input().split()))
    A.sort()
    print(A[2] + A[3])

=======
Suggestion 4

def main():
    A = list(map(int, input().split()))
    print(min(A))

=======
Suggestion 5

def main():
    a = list(map(int, input().split()))
    print(min(a))

=======
Suggestion 6

def main():
    a = list(map(int, input().split()))
    a.sort()
    print(a[0])

=======
Suggestion 7

def problems185_a():
    A = [int(i) for i in input().split()]
    A.sort()
    print(A[0])

=======
Suggestion 8

def main():
    A = list(map(int, input().split()))
    print(min(A))

main()
