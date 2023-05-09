Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    if N*M - sum(A) > K:
        print(-1)
    elif N*M - sum(A) > 0:
        print(N*M - sum(A))
    else:
        print(0)

=======
Suggestion 2

def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n-1):
        sum += a[i]
    if n*m - sum > k:
        print(-1)
    else:
        if n*m - sum > 0:
            print(n*m - sum)
        else:
            print(0)

=======
Suggestion 3

def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    x = n*m - sum(a)
    if x > k:
        print(-1)
    elif x < 0:
        print(0)
    else:
        print(x)

=======
Suggestion 4

def problems151_b():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    if n*m - sum(a) > k:
        print(-1)
    else:
        print(max(0, n*m - sum(a)))

=======
Suggestion 5

def problem151_b():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    print(max(0, N*M - sum(A)) if max(0, N*M - sum(A)) <= K else -1)

=======
Suggestion 6

def problems151_b():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))

    if (N * M) - sum(A) > K:
        print(-1)
    else:
        print(max(0, (N * M) - sum(A)))

=======
Suggestion 7

def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    total = sum(a)
    if n*m - total > k:
        print(-1)
    elif n*m - total < 0:
        print(0)
    else:
        print(n*m - total)

=======
Suggestion 8

def main():
    n,k,m = map(int,input().split())
    a = list(map(int,input().split()))
    x = m*n
    y = sum(a)
    z = x - y
    if z > k:
        print(-1)
    elif z <= 0:
        print(0)
    else:
        print(z)

=======
Suggestion 9

def get_input():
    n,k,m = map(int, input().split())
    a = list(map(int, input().split()))
    return n,k,m,a

=======
Suggestion 10

def main():
    # Get input here
    N, K, M = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))

    # Calculate the result
    result = 0
    for i in range(N - 1):
        result += A[i]
    if result >= M * N:
        result = 0
    elif M * N - result > K:
        result = -1
    else:
        result = M * N - result

    # Print the result
    print(result)
