Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] > X:
            ans += A[i] - X
    print(max(ans - K * X, 0))

=======
Suggestion 2

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] <= X:
            ans += A[i]
        else:
            ans += X
    ans -= K * X
    if ans < 0:
        ans = 0
    print(ans)

=======
Suggestion 3

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += max(A[i] - K * X, 0)
    print(ans)

=======
Suggestion 4

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for a in A:
        ans += max(a - K * X, 0)
    print(ans)

=======
Suggestion 5

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += max(A[i] - X * K, 0)
    print(ans)

=======
Suggestion 6

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if i < K:
            ans += max(A[i] - X, 0)
        else:
            ans += A[i]
    print(ans)

=======
Suggestion 7

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N-K):
        ans += max(A[i]-X, 0)
    for i in range(N-K, N):
        ans += A[i]
    print(ans)

=======
Suggestion 8

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    total = 0
    for i in range(N):
        if i < K:
            total += max(A[i] - X, 0)
        else:
            total += A[i]
    print(total)

=======
Suggestion 9

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()

    ans = 0
    for i in range(N):
        if i < K:
            ans += max(A[i] - X, 0)
        else:
            ans += A[i]

    print(ans)

=======
Suggestion 10

def main():
    N,K,X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if K > 0:
            if A[i] > X:
                ans += X
                K -= 1
            else:
                ans += A[i]
        else:
            ans += A[i]
    print(ans)
