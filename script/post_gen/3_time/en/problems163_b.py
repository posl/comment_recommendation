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
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    print(n - sum(a) if n >= sum(a) else -1)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    print(N - sum(A) if N >= sum(A) else -1)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    if N >= sum(A):
        print(N - sum(A))
    else:
        print("-1")

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    print(max(n - sum(a), -1))

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    if n < sum(a):
        print(-1)
    else:
        print(n-sum(a))

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    print(max(N-sum(A), -1))

=======
Suggestion 8

def solve(n, m, a):
    if sum(a) > n:
        return -1
    else:
        return n - sum(a)
