Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] > X:
            ans += X
            K -= 1
        else:
            ans += A[i]
    if K > 0:
        ans += X * K
    print(ans)

=======
Suggestion 2

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] > X:
            ans += A[i] - K * X
        else:
            ans += A[i]
    print(ans)

=======
Suggestion 3

def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] > x:
            ans += a[i] - x
    print(ans)

=======
Suggestion 4

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += max(A[i] - X * K, 0)
    print(ans)

=======
Suggestion 5

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for a in A:
        ans += max(a - K*X, 0)
    print(ans)

=======
Suggestion 6

def solve():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] > X:
            ans += A[i] - X
    print(max(0, ans - K))

=======
Suggestion 7

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = max(A[i] - X * K, 0)
    print(sum(B))

=======
Suggestion 8

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    sum = 0
    for i in range(N):
        if i < K:
            sum += max(A[i] - X, 0)
        else:
            sum += A[i]
    print(sum)

=======
Suggestion 9

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    #print(A)
    for i in range(N):
        if i < K:
            A[i] = max(A[i] - X, 0)
    print(sum(A))
