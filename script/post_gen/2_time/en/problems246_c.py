Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += max(A[i]-K*X, 0)
    return ans

print(solve())

=======
Suggestion 2

def solve():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += max(A[i] - K * X, 0)
    print(ans)

solve()

=======
Suggestion 3

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += min(A[i], K) * (X if A[i] > K else 0)
    print(ans)

=======
Suggestion 4

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] < X:
            ans += A[i]
        else:
            ans += X
    print(ans)

=======
Suggestion 5

def main():
    N, K, X = map(int, input().split())
    A = map(int, input().split())
    total = 0
    for a in A:
        total += max(a - X, 0)
    print(total)

=======
Suggestion 6

def main():
    n,k,x = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += max(a[i]-k*x,0)
    print(ans)

=======
Suggestion 7

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if K * X >= sum(A):
        print(0)
    else:
        print(sum(A) - (K * X))

=======
Suggestion 8

def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(sum([min(x, ai) for ai in a]))

=======
Suggestion 9

def main():
    N, K, X = map(int, input().split())
    A = [int(x) for x in input().split()]
    sum = 0
    for i in range(0,N):
        if A[i] < K:
            sum += A[i]
        else:
            sum += K
    print(sum)

=======
Suggestion 10

def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(sum([min(x, i) for i in a]) - k * x)
