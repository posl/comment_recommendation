Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(a[-2])

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[-2])

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    print(a[1])

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(a[n-2])

=======
Suggestion 5

def booby_prize():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = sorted(A, reverse=True)
    for i in range(N):
        if A[i] == B[1]:
            return i + 1

print(booby_prize())

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(a[-2])
main()

=======
Suggestion 7

def get_input():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a
