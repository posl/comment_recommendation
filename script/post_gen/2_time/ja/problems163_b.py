Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    if sum(A) > N:
        print(-1)
    else:
        print(N - sum(A))

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(M):
        N -= A[i]
        if N < 0:
            print(-1)
            return
    print(N)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(M):
        N -= A[i]
        if N < 0:
            print(M - i)
            return
    print(-1)

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(m):
        n -= a[i]
        if n < 0:
            print(i)
            return
    print(n)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    for a in A:
        N -= a
        if N < 0:
            print(-1)
            return
    print(N)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if N < sum(A):
        print(-1)
    else:
        print(N - sum(A))

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if sum(A) > N:
        print(-1)
    else:
        print(N - sum(A))

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = N
    for i in range(M):
        ans -= A[i]
        if ans < 0:
            print("-1")
            return
    print(ans)

=======
Suggestion 9

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    sumA = sum(A)
    if sumA > N:
        print(-1)
    else:
        print(N-sumA)
