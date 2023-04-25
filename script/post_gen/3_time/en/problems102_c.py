Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [A[i] - (i + 1) for i in range(N)]
    A.sort()
    b = A[N // 2]
    ans = sum([abs(A[i] - b) for i in range(N)])
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [A[i] - (i + 1) for i in range(N)]
    A.sort()
    b = A[N // 2]
    ans = 0
    for i in range(N):
        ans += abs(A[i] - b)
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a - i - 1 for i, a in enumerate(A)]
    A.sort()
    b = A[N//2]
    ans = sum(abs(a - b) for a in A)
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    b = A[N//2]
    ans = 0
    for i in range(N):
        ans += abs(A[i] - b - i + N//2)
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [a[i] - (i + 1) for i in range(n)]
    a.sort()
    med = a[n // 2]
    ans = sum([abs(med - a[i]) for i in range(n)])
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A = [A[i] - i - 1 for i in range(N)]
    A.sort()
    b = A[N//2]
    print(sum([abs(a - b) for a in A]))

=======
Suggestion 7

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A = [x - (i + 1) for i, x in enumerate(A)]
    A.sort()
    if N % 2 == 1:
        b = A[N//2]
    else:
        b = (A[N//2-1] + A[N//2]) // 2
    print(sum([abs(x - b) for x in A]))

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if N%2 == 0:
        print(sum(A[N//2:]) - sum(A[:N//2]))
    else:
        print(sum(A[N//2+1:]) - sum(A[:N//2]))

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [A[i] - i for i in range(N)]
    A.sort()
    b = A[N // 2]

    ans = 0
    for i in range(N):
        ans += abs(A[i] - b)

    print(ans)

=======
Suggestion 10

def main():
    # input
    N = int(input())
    As = [*map(int, input().split())]

    # compute
    As = [A-i for i, A in enumerate(As, start=1)]
    As.sort()
    if N % 2 == 0:
        b = (As[N//2-1] + As[N//2]) // 2
    else:
        b = As[N//2]

    # output
    print(sum(abs(A-b) for A in As))
