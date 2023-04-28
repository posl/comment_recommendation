Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    max_dist = 0
    for i in range(N-1):
        max_dist = max(max_dist, A[i+1] - A[i])
    max_dist = max(max_dist, K - A[N-1] + A[0])
    print(K - max_dist)

=======
Suggestion 2

def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    max_dist = 0
    for i in range(n - 1):
        max_dist = max(max_dist, a[i + 1] - a[i])
    max_dist = max(max_dist, k - a[n - 1] + a[0])
    print(k - max_dist)

=======
Suggestion 3

def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n - 1):
        b[i] = a[i + 1] - a[i]
    b[n - 1] = k - a[n - 1] + a[0]
    print(k - max(b))

=======
Suggestion 4

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(A[0] + K)
    max_d = 0
    for i in range(N):
        d = A[i+1] - A[i]
        if max_d < d:
            max_d = d
    print(K - max_d)

=======
Suggestion 5

def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(a[0] + k)
    print(k - max([a[i+1] - a[i] for i in range(n)]))

=======
Suggestion 6

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(A[0] + K)
    dist = [A[i+1] - A[i] for i in range(N)]
    print(K - max(dist))

=======
Suggestion 7

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(A[0]+K)
    d = [A[i+1]-A[i] for i in range(N)]
    print(K - max(d))

=======
Suggestion 8

def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    B = [K]
    for i in range(1, N):
        B.append(A[i] - A[i - 1])
    print(K - max(B))

main()

=======
Suggestion 9

def main():
    # input
    K, N = map(int, input().split())
    A = list(map(int, input().split()))

    # compute
    d = [0] * N
    for i in range(N-1):
        d[i] = A[i+1] - A[i]
    d[N-1] = K - A[N-1] + A[0]
    d.sort()
    ans = 0
    for i in range(N-1):
        ans += d[i]

    # output
    print(ans)

=======
Suggestion 10

def main():
    # input
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    # compute
    A.append(A[0]+K)
    max_dist = 0
    for i in range(N):
        max_dist = max(max_dist, A[i+1]-A[i])
    # output
    print(K-max_dist)
