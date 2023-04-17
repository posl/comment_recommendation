Synthesizing 10/10 solutions (Duplicates hidden)

=======

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += abs(A[i] - (i+1))
    print(ans)

=======

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [A[i] - i - 1 for i in range(N)]
    B.sort()
    b = B[N // 2]
    ans = 0
    for i in range(N):
        ans += abs(B[i] - b)
    print(ans)

=======

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [A[i] - i - 1 for i in range(N)]
    A.sort()
    if N % 2 == 1:
        median = A[N // 2]
    else:
        median = (A[N // 2 - 1] + A[N // 2]) // 2
    ans = 0
    for i in range(N):
        ans += abs(A[i] - median)
    print(ans)

=======

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = sorted(A)
    ans = 0
    for i in range(N):
        ans += abs(A[i] - (i+1))
    print(ans)

=======

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [A[i] - i for i in range(N)]
    A.sort()
    b = A[N//2]
    ans = 0
    for i in range(N):
        ans += abs(A[i] - b)
    print(ans)

=======

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if N % 2 == 0:
        print(sum(A[N//2:])-sum(A[:N//2]))
    else:
        print(sum(A[N//2+1:])-sum(A[:N//2]))

=======

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a-i for i, a in enumerate(A)]
    A.sort()
    ans = 0
    for a in A:
        ans += abs(A[N//2] - a)
    print(ans)

=======

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    mid = N // 2
    if N % 2 == 0:
        ans = 2 * sum(A[mid:]) - sum(A[:mid]) - A[mid] - A[mid-1]
    else:
        ans = 2 * sum(A[mid+1:]) - sum(A[:mid]) - A[mid] - A[mid+1]
    print(ans)

=======

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = n // 2
    print(sum(a[b:]) - sum(a[:b]))
