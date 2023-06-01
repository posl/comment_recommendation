Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if sum(A) <= N:
        print(N - sum(A))
    else:
        print(-1)

=======
Suggestion 2

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    if sum(a) > n:
        print(-1)
    else:
        print(n - sum(a))

solve()

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    if sum(a) > n:
        print(-1)
    else:
        print(n - sum(a))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    if sum(A) > N:
        print(-1)
    else:
        print(N - sum(A))

=======
Suggestion 5

def solve(n, m, a):
    if n < sum(a):
        return -1
    else:
        return n - sum(a)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    print(n - sum(a) if n >= sum(a) else -1)

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    total = sum(a)
    if total > n:
        print(-1)
    else:
        print(n - total)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    sum = 0
    for i in range(M):
        sum += A[i]
    if sum == N:
        print(0)
    elif sum > N:
        print(-1)
    else:
        print(N - sum)

=======
Suggestion 9

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    if sum(a) > n:
        print(-1)
        return
    print(n - sum(a))
