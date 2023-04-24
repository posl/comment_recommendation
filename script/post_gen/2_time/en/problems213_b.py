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
    N = int(input())
    A = list(map(int, input().split()))
    A_sorted = sorted(A)
    print(A.index(A_sorted[1]) + 1)

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
    A = list(map(int,input().split()))
    min_a = min(A)
    A.remove(min_a)
    print(A.index(min(A))+1)

main()
