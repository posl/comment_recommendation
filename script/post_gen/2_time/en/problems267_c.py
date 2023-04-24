Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N - M + 1):
        ans = max(ans, sum(A[i:i + M]) * M)
    print(ans)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n - m + 1):
        ans = max(ans, sum([j * a[i + j] for j in range(m)]))
    print(ans)

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    sum_a = [0]
    for i in range(n):
        sum_a.append(sum_a[-1] + a[i])
    ans = - 2 * 10**5 * n
    for i in range(n - m + 1):
        ans = max(ans, sum_a[i + m] - sum_a[i])
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    if N == M:
        ans = 0
        for i in range(N):
            ans += (i+1) * A[i]
        print(ans)
        return
    ans = -float("inf")
    for i in range(N-M+1):
        for j in range(i+M, N+1):
            tmp = 0
            for k in range(i, j):
                tmp += (k-i+1) * A[k]
            ans = max(ans, tmp)
    print(ans)
    return

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # B = [0] * N
    # for i in range(N):
    #     B[i] = A[i]
    #     if i >= M:
    #         B[i] += B[i - M]
    # B.sort(reverse=True)
    # print(sum([i * B[i] for i in range(M)]))
    B = [0] * (N - M + 1)
    for i in range(N - M + 1):
        B[i] = sum(A[i:i + M])
    B.sort(reverse=True)
    print(sum([i * B[i] for i in range(M)]))

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, M, A)
    B = []
    for i in range(N):
        if i == 0:
            B.append(A[i])
        else:
            B.append(B[i-1] + A[i])
    #print(B)
    C = []
    for i in range(N-M+1):
        if i == 0:
            C.append(B[i+M-1])
        else:
            C.append(B[i+M-1] - B[i-1])
    #print(C)
    D = []
    for i in range(N-M+1):
        if i == 0:
            D.append(i+1)
        else:
            D.append(D[i-1] + 1)
    #print(D)
    E = []
    for i in range(N-M+1):
        E.append(C[i] * D[i])
    #print(E)
    print(max(E))

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # print(N, M)
    # print(A)
    B = sorted(A, reverse=True)
    # print(B)
    ans = 0
    for i in range(M):
        ans += B[i]
    print(ans)

=======
Suggestion 8

def solve(N,M,A):
    B = [0 for i in range(N)]
    for i in range(N):
        B[i] = A[i] + (B[i-1] if i > 0 else 0)
    ans = 0
    for i in range(M,N+1):
        ans = max(ans, B[i-1] - (B[i-M-1] if i > M else 0))
    return ans

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # 1-indexed
    A = [0] + A
    # A[i] - A[i-1] の値を格納
    # [0, A[1] - A[0], A[2] - A[1], ..., A[N] - A[N-1]]
    # これを累積和し、M個ずつの累積和の最大値を求める
    diff = [0] * (N + 1)
    for i in range(1, N + 1):
        diff[i] = A[i] - A[i - 1]
    # print(diff)
    # 累積和
    for i in range(1, N + 1):
        diff[i] += diff[i - 1]
    # print(diff)
    # M個ずつの累積和の最大値を求める
    ans = 0
    for i in range(M, N + 1):
        ans = max(ans, diff[i] - diff[i - M])
    print(ans)

=======
Suggestion 10

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    #print(n, m)
    #print(a)
    
    #b = [0] * (n-m+1)
    b = []
    for i in range(n-m+1):
        b.append(sum(a[i:i+m]))
    #print(b)
    b.sort()
    #print(b)
    #print(b[-1])
    ans = 0
    for i in range(m):
        ans += (i+1) * b[-1]
    print(ans)
    
solve()
