Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(a[n-1])

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[N-1])

=======
Suggestion 3

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[N-1])

=======
Suggestion 4

def solve():
    N = int(input())
    A = list(map(int,input().split()))
    a = set()
    for i in range(4*N-1):
        if A[i] in a:
            a.remove(A[i])
        else:
            a.add(A[i])
    print(a.pop())

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[(2*N)-1])

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(0, len(A), 2):
        if A[i] != A[i+1]:
            print(A[i])
            break

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[int(len(A)/2)])
