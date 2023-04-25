Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    for i in range(N):
        B[i + 1] = B[i] + A[i]
    D = {}
    for i in range(N + 1):
        if B[i] % M in D:
            D[B[i] % M].append(i)
        else:
            D[B[i] % M] = [i]
    ans = 0
    for i in range(M):
        if i in D:
            for j in range(len(D[i]) - 1):
                ans = max(ans, (D[i][j + 1] - D[i][j]) // M)
    print(ans * M)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N - M + 1):
        ans = max(ans, sum([x * (i + 1) for i, x in enumerate(A[i:i + M])]))
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * (N - M + 1)
    for i in range(N - M + 1):
        B[i] = sum(A[i:i + M])
    print(sum(range(1, M + 1)) * max(B))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    sumA = [0] * (N + 1)
    for i in range(N):
        sumA[i + 1] = sumA[i] + A[i]
    ans = float('-inf')
    for i in range(N - M + 1):
        ans = max(ans, sumA[i + M] - sumA[i] + M * A[i])
    print(ans)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * (n - m + 1)
    for i in range(n - m + 1):
        b[i] = sum(a[i:i+m])
    b.sort()
    ans = 0
    for i in range(m):
        ans += (i + 1) * b[n - m - i]
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = (i + 1) * A[i] - (i) * A[i]
    ans = 0
    for i in range(N - M + 1):
        ans = max(ans, sum(B[i:i + M]))
    print(ans)

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[i] = a[i] - a[i - 1]
    b.pop(0)
    b.sort(reverse=True)
    print(sum(b[:n - m]))

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = sum(a[:m])
    ans = s
    for i in range(1, n - m + 1):
        s += a[m + i - 1] - a[i - 1]
        ans = max(ans, s)
    print(ans)

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    s = sum(a[:m])
    ans = s
    for i in range(n-m):
        s += a[i+m]
        s -= a[i]
        ans = max(ans,s)
    print(ans)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    # 1. A[i] + A[i+1] + ... + A[j] = S[j] - S[i-1]
    # 2. sum_{i=1}^{M} i × B_i = M × (M+1) / 2 + (S[j] - S[i-1]) × (M+1)
    # 3. sum_{i=1}^{M} i × B_i = M × (M+1) / 2 + (S[j] - S[i-1]) × (M+1) - M × (M+1) / 2 = (S[j] - S[i-1]) × (M+1)
    # 4. sum_{i=1}^{M} i × B_i = (S[j] - S[i-1]) × (M+1)
    # 5. sum_{i=1}^{M} i × B_i = S[j] × (M+1) - S[i-1] × (M+1)
    # 6. sum_{i=1}^{M} i × B_i = S[j] × (M+1) - S[i-1] × (M+1) + M × (M+1) / 2
    # 7. sum_{i=1}^{M} i × B_i = S[j] × (M+1) - S[i-1] × (M+1) + M × (M+1) / 2 - M × (M+1) / 2 = S[j] × (M+1) - S[i-1] × (M+1)
    # 8. sum_{i=1}^{M} i × B_i = (S[j] - S[i-1]) × (M+1)
    # 9. sum_{i=1}^{M} i × B_i = (S[j] - S[i-1]) × (M+1) + S[i-1] × (M+1) - S[j] × (M+1)
    #10. sum_{i=1}^{M} i × B_i = (S[j]
