Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a)
    print(a.index(b[1])+1)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a_sorted = sorted(a)
    print(a.index(a_sorted[1])+1)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(a[1])

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
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    print(a[1])

=======
Suggestion 7

def problem213_b():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    sorted_A = sorted(A)
    #print(sorted_A)
    print(A.index(sorted_A[1]) + 1)
