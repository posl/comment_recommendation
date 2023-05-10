Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a = list(map(int, input().split()))
    a.sort()
    print(a[2] - a[0])

=======
Suggestion 2

def main():
    A = list(map(int, input().split()))
    A.sort()
    print(A[2]-A[0])

=======
Suggestion 3

def main():
    a, b, c = map(int, input().split())
    print(max(a, b, c) - min(a, b, c))

=======
Suggestion 4

def main():
    # input
    A_1, A_2, A_3 = map(int, input().split())

    # compute

    # output
    print(max(A_1, A_2, A_3) - min(A_1, A_2, A_3))

=======
Suggestion 5

def solve():
    a = list(map(int, input().split()))
    a.sort()
    print(a[2] - a[0])
