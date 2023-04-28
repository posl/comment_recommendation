Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    a_sum = sum(a_list)
    if n >= a_sum:
        print(n - a_sum)
    else:
        print(-1)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    if N < sum(A):
        print(-1)
    else:
        print(N-sum(A))

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    total = sum(A)
    if N < total:
        print(-1)
    else:
        print(N - total)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    sum = 0
    for i in range(M):
        sum += A[i]
    if sum > N:
        print(-1)
    else:
        print(N - sum)

=======
Suggestion 5

def solve():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    if sum(A) > N:
        return -1
    else:
        return N - sum(A)

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    ans = 0
    for i in range(m):
        ans += a[i]
    if ans > n:
        ans = -1
    print(ans)

=======
Suggestion 7

def solve(N, M, A):
    if N < sum(A):
        return -1
    else:
        return N - sum(A)

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    total = sum(a)
    if n < total:
        print(-1)
    else:
        print(n-total)

=======
Suggestion 9

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    s = sum(a)
    if s < n:
        return -1
    for i in range(m):
        if a[i] < n:
            return i + 1
    return m

print(solve())

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    print(max(n-sum(a),-1))
