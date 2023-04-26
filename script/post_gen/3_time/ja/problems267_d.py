Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N - M + 1):
        ans = max(ans, sum(j * A[i + j - 1] for j in range(1, M + 1)))
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    for i in range(N):
        B[i + 1] = B[i] + A[i]
    ans = 0
    for i in range(N - M + 1):
        for j in range(i + M, N + 1):
            ans = max(ans, (B[j] - B[i]) * M)
    print(ans)

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * (n - m + 1)
    for i in range(n - m + 1):
        b[i] = sum(a[i:i + m])
    c = []
    for i in range(n - m + 1):
        c.append(b[i] + sum(a[i + m:]))
    print(max(c))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * (N - M + 1)

    for i in range(N - M + 1):
        B[i] = sum(A[i:i + M])

    print(max(B))

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = sum(A[:i+1])
    C = [0] * (N-M+1)
    for i in range(N-M+1):
        C[i] = sum(B[i:i+M])
    print(max(C))

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = -float("inf")
    for i in range(N-M+1):
        for j in range(i+M, N+1):
            ans = max(ans, sum(A[i:j]) * M)
            M -= 1
    print(ans)

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(m):
        ans += (i+1)*a[n-m+i]
    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, M)
    #print(A)
    ans = 0
    for i in range(N):
        for j in range(i+1, N+1):
            if j-i < M:
                continue
            #print(i, j)
            B = A[i:j]
            #print(B)
            B.sort(reverse=True)
            #print(B)
            tmp = 0
            for k in range(M):
                tmp += (k+1) * B[k]
            #print(tmp)
            ans = max(ans, tmp)
    print(ans)

=======
Suggestion 9

def main():
    from sys import stdin
    def input():
        return stdin.readline().strip()
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(n-m+1):
        ans = max(ans, sum([(j+1)*a[i+j] for j in range(m)]))
    print(ans)

=======
Suggestion 10

def read_ints():
    return list(map(int, input().split()))
