Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += max(0, A[i] - K * X)
    print(ans)

=======
Suggestion 2

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for a in A:
        ans += max(a - K * X, 0)
    print(ans)

=======
Suggestion 3

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += max(A[i] - K * X, 0)
    print(ans)

=======
Suggestion 4

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += max(A[i] - X * K, 0)
    print(ans)

=======
Suggestion 5

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
Suggestion 6

def main():
    N, K, X = map(int, input().split())
    A = [int(n) for n in input().split()]
    ans = 0
    for i in range(N):
        ans += max(A[i] - K*X, 0)
    print(ans)

=======
Suggestion 7

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A
    ans = 0
    for i in range(N):
        if A[i+1] - A[i] > X:
            ans += (A[i+1] - A[i]) // X
            if (A[i+1] - A[i]) % X == 0:
                ans -= 1
    if ans <= K:
        print(0)
    else:
        print(ans - K)

=======
Suggestion 8

def main():
    N,K,X = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    ans = 0
    for i in range(N):
        if i < K:
            ans += max(A[i] - X,0)
        else:
            ans += A[i]

    print(ans)

=======
Suggestion 9

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()

    for i in range(N):
        if A[i] <= X:
            K -= 1
            A[i] = 0
        else:
            break

    if K <= 0:
        print(sum(A))
    else:
        A = [max(a - K * X, 0) for a in A]
        print(sum(A))

=======
Suggestion 10

def solve(N, K, X, A):
    A = sorted(A)
    A = [0] + A
    ans = 0
    for i in range(N, 0, -1):
        if A[i] - A[i - 1] <= K * X:
            K -= (A[i] - A[i - 1]) // X
            ans += A[i] - A[i - 1]
        else:
            ans += K * X
            K = 0
            break
    ans += K * X
    return ans
