Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += max(A[i] - K * X, 0)
    print(ans)

=======
Suggestion 2

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = 0
    for i in range(N):
        if i < K:
            ans += max(A[i] - X, 0)
        else:
            ans += A[i]
    print(ans)

=======
Suggestion 3

def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    s = 0
    for i in range(n):
        s += max(a[i] - k * x, 0)
    print(s)

=======
Suggestion 4

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse = True)
    ans = 0
    for i in range(N):
        if K > 0:
            ans += max(A[i] - X, 0)
            K -= 1
        else:
            ans += A[i]
    print(ans)

=======
Suggestion 5

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
Suggestion 6

def solve():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = max(A[i] - X * K, 0)
    print(sum(B))

=======
Suggestion 7

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    total = 0
    for i in range(N):
        if i < K:
            total += max(A[i] - X, 0)
        else:
            total += A[i]
    print(total)

main()

=======
Suggestion 8

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    print(sum([max(A[i] - X * K, 0) for i in range(N)]))

=======
Suggestion 9

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    for i in range(N):
        if A[i] >= X:
            A[i] -= X
            K -= 1
        else:
            break
    if K > 0:
        for i in range(N):
            if A[i] > 0:
                if K >= A[i] // X:
                    K -= A[i] // X
                    A[i] %= X
                else:
                    A[i] -= K * X
                    K = 0
    print(sum(A))

=======
Suggestion 10

def main():
    #input
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    #solve
    for i in range(N):
        if A[i] > X:
            A[i] = X
    #output
    print(sum(A))
