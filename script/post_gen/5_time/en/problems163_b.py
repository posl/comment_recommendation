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
    if N < sum(A):
        print(-1)
    else:
        print(N - sum(A))

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    total = sum(a)
    if total > n:
        print(-1)
    else:
        print(n - total)

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    print(n - sum(a) if n >= sum(a) else -1)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    sum_A = sum(A)
    if sum_A > N:
        print(-1)
    else:
        print(N-sum_A)

=======
Suggestion 6

def solve():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    if N < sum(A):
        print(-1)
    else:
        print(N-sum(A))

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    print(n - sum(a) if n >= sum(a) else -1)

=======
Suggestion 8

def calc_days(N, M, A):
    if N < sum(A):
        return -1
    return N - sum(A)

N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
print(calc_days(N, M, A))
