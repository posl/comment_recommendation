Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    if sum(a) > n:
        print(-1)
    else:
        print(n - sum(a))

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
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    print(n - sum(a) if n >= sum(a) else -1)

=======
Suggestion 4

def problem163_b():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    if n >= sum(a):
        print(n - sum(a))
    else:
        print(-1)

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    if n < sum(a):
        print(-1)
    else:
        print(n-sum(a))

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    for i in range(M):
        N -= A[i]
        if N < 0:
            print(-1)
            break
    else:
        print(N)

=======
Suggestion 7

def main():
    # input
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    # compute

    # output
    print(max(n - sum(a), -1))

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    N -= sum(A)
    if N < 0:
        N = -1
    print(N)

=======
Suggestion 9

def max_hang_out_days(n, m, a):
    if n < sum(a):
        return -1
    else:
        return n - sum(a)
