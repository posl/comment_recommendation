Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    for i in range(M):
        A[0] = A[0] // 2
        A.sort(reverse=True)
    print(sum(A))

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    for i in range(m):
        a[0] = a[0] // 2
        a.sort(reverse=True)
    print(sum(a))

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    for i in range(M):
        A[i] = A[i] // 2
    A.sort(reverse=True)
    print(sum(A))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(M):
        A[-1] //= 2
        A.sort()
    print(sum(A))

=======
Suggestion 5

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for _ in range(M):
        A[-1] = A[-1] // 2
        A.sort()
    print(sum(A))

=======
Suggestion 6

def problem():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    for i in range(m):
        a[0] = a[0]//2
        a.sort(reverse=True)
    print(sum(a))

problem()

=======
Suggestion 7

def get_input():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    return n,m,a

=======
Suggestion 8

def main():
    # Get input
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    # Sort the list
    A.sort(reverse = True)

    # Calculate the sum
    sum = 0
    for i in range(N):
        sum += A[i]

    # Calculate the minimum amount of money required
    for i in range(M):
        sum -= A[i] / 2**(i+1)

    # Output the answer
    print(int(sum))
