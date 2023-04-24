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
    if sum(a) > n:
        print(-1)
    else:
        print(n - sum(a))

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    if N < sum(A):
        print(-1)
    else:
        print(N - sum(A))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    total = sum(A)
    if total > N:
        print(-1)
    else:
        print(N - total)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    if sum(A) > N:
        print(-1)
        return
    else:
        print(N - sum(A))

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if sum(a) > n:
        print(-1)
    else:
        print(n - sum(a))

=======
Suggestion 7

def main():
    # Input
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # Solve
    if sum(A) > N:
        ans = -1
    else:
        ans = N - sum(A)
    # Output
    print(ans)
