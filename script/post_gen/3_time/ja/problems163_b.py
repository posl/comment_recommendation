Synthesizing 10/10 solutions

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
    if sum(A) <= N:
        print(N - sum(A))
    else:
        print(-1)

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
            break
    else:
        print(-1)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()

    for i in range(M):
        N -= A[i]
        if N < 0:
            print(-1)
            return

    if N == 0:
        print(0)
    else:
        print(N)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(M):
        if A[i] <= N:
            N -= A[i]
        else:
            print(N)
            return
    print(-1)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    for i in range(M):
        N -= A[i]
        if N < 0:
            print(-1)
            return
    print(N)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    for i in range(M):
        N -= A[i]
        if N < 0:
            print(i)
            exit()
    print(-1)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = A[::-1]
    for i in range(M):
        N -= A[i]
        if N <= 0:
            if N == 0:
                print(0)
            else:
                print(-1)
            return
    print(N)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    As = list(map(int, input().split()))
    As.sort(reverse=True)
    for A in As:
        N -= A
        if N < 0:
            print(-1)
            return
    print(N)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    total = 0
    for a in A:
        total += a
    if total > N:
        print(-1)
    else:
        print(N-total)
