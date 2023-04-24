Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += (i + 1) * (N - i) * A[i]
    ans = ans // N
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = sorted(A)
    C = [0] * (N + 1)
    for i in range(N):
        C[i + 1] = C[i] + B[i]
    D = [0] * (N + 1)
    for i in range(N):
        D[i + 1] = D[i] + A[i]
    E = [0] * (N + 1)
    for i in range(N):
        E[i + 1] = E[i] + (B[N // 2] - B[i])
    F = [0] * (N + 1)
    for i in range(N):
        F[i + 1] = F[i] + (B[N // 2 - 1] - B[i])
    G = [0] * (N + 1)
    for i in range(N):
        G[i + 1] = G[i] + (A[i] - B[N // 2])
    H = [0] * (N + 1)
    for i in range(N):
        H[i + 1] = H[i] + (A[i] - B[N // 2 - 1])
    ans = 0
    for i in range(N):
        ans += A[i] * (N - i) * (i + 1)
    for i in range(N):
        ans -= (C[i + 1] + D[N] - D[i + 1]) * (N - i)
        ans -= (C[N] - C[i + 1] + D[N] - D[i + 1]) * (i + 1)
        ans += (E[i + 1] + F[N] - F[i + 1]) * (N - i)
        ans += (E[N] - E[i + 1] + F[N] - F[i + 1]) * (i + 1)
        ans -= (G[i + 1] + H[N] - H[i + 1]) * (N - i)
        ans -= (G[N] - G[i + 1] + H[N] - H[i + 1]) * (i + 1)
    print(ans // (2 * N))

=======
Suggestion 3

def median(a):
    a.sort()
    return a[len(a)//2]

n = int(input())
a = list(map(int, input().split()))
m = []
for i in range(n):
    for j in range(i+1, n+1):
        m.append(median(a[i:j]))
print(median(m))

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    M = N * (N + 1) // 2
    M2 = (M + 1) // 2
    M3 = (M + 2) // 2
    B = []
    for i in range(N):
        B.append((A[i], i))
    B.sort()
    C = [0] * N
    for i in range(M):
        C[B[i][1]] = i
    S = [0] * (N + 1)
    S2 = [0] * (N + 1)
    S3 = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + C[i]
        S2[i + 1] = S2[i] + (C[i] < M2)
        S3[i + 1] = S3[i] + (C[i] < M3)
    ans = 0
    for i in range(N):
        ans += (S2[N] - S2[i]) * (C[i] + 1) - (S[i + 1] - S2[i])
        ans += (S[i + 1] - S3[i]) - (S3[N] - S3[i]) * (C[i] + 1)
    ans //= M
    print(ans)

main()

=======
Suggestion 5

def median(a):
    a.sort()
    return a[len(a) // 2]

n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    ans += median(a[:i+1]) * (i + 1) - median(a[:i]) * i
print(ans)

n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    ans += median(a[i:]) * (i + 1) - median(a[i+1:]) * i
print(ans)

n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    ans += median(a[:i+1]) * (i + 1) - median(a[:i]) * i
    ans += median(a[i:]) * (i + 1) - median(a[i+1:]) * i
print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = i + 1
    C = [0] * N
    for i in range(N):
        C[i] = N - i
    D = [0] * N
    for i in range(N):
        D[i] = (i + 1) * (N - i)
    E = [0] * N
    for i in range(N):
        E[i] = A[i] * D[i]
    E.sort()
    F = [0] * N
    for i in range(N):
        F[i] = E[i] // D[i]
    print(F[(N - 1) // 2])

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(median(A))

=======
Suggestion 8

def solve(N, a):
    a.sort()
    ans = 0
    for i in range(N):
        ans += a[i] * (i * 2 - N + 1)
    return ans

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    #print(N)
    #print(A)
    if N % 2 == 0:
        print(A[N // 2 - 1])
    else:
        print(A[N // 2])

=======
Suggestion 10

def median(l):
    l.sort()
    return l[len(l)//2]
