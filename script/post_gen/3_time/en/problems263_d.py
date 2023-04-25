Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] < L:
            ans += L
        elif A[i] > R:
            ans += R
        else:
            ans += A[i]
    print(ans)

=======
Suggestion 2

def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] < l:
            ans += l
        elif a[i] > r:
            ans += r
        else:
            ans += a[i]
    print(ans)

=======
Suggestion 3

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += min(max(A[i], L), R)
    print(ans)

=======
Suggestion 4

def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if i < n // 2:
            ans += min(l, a[i])
        else:
            ans += min(r, a[i])
    print(ans)

=======
Suggestion 5

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if i < N // 2:
            ans += min(A[i], L)
        else:
            ans += min(A[i], R)
    print(ans)

=======
Suggestion 6

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    print(sum(A[:N//2]) * L + sum(A[N//2:]) * R)

=======
Suggestion 7

def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] * ((n-i-1) * r + (i) * l) // n
        ans -= a[i] * ((n-i-1) * l + (i) * r) // n
    print(ans)

=======
Suggestion 8

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = A[:N//2]
    C = A[N//2:]
    print(sum(B)*L + sum(C)*R)
