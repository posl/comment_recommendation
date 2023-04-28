Synthesizing 10/10 solutions

=======
Suggestion 1

def readinput():
    n,m,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    return n,m,k,a,b

=======
Suggestion 2

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    for i in range(1, N):
        A[i] += A[i-1]
    for i in range(1, M):
        B[i] += B[i-1]

    ans, j = 0, M
    for i in range(N):
        if A[i] > K:
            break
        while j > 0 and A[i] + B[j-1] > K:
            j -= 1
        ans = max(ans, i + j + 1)

    print(ans)

=======
Suggestion 3

def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a = [0] + a
    b = [0] + b

    for i in range(n):
        a[i+1] += a[i]
    for i in range(m):
        b[i+1] += b[i]

    ans = 0
    j = m
    for i in range(n+1):
        if a[i] > k:
            break
        while b[j] > k - a[i]:
            j -= 1
        ans = max(ans, i+j)
    print(ans)

=======
Suggestion 4

def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a_sum = [0]
    b_sum = [0]
    for i in range(n):
        a_sum.append(a_sum[i] + a[i])
    for i in range(m):
        b_sum.append(b_sum[i] + b[i])

    ans = 0
    j = m
    for i in range(n + 1):
        if a_sum[i] > k:
            break
        while b_sum[j] > k - a_sum[i]:
            j -= 1
        ans = max(ans, i + j)
    print(ans)

=======
Suggestion 5

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A_sum = [0]
    B_sum = [0]
    for i in range(N):
        A_sum.append(A_sum[i] + A[i])
    for i in range(M):
        B_sum.append(B_sum[i] + B[i])
    ans = 0
    j = M
    for i in range(N+1):
        if A_sum[i] > K:
            break
        while B_sum[j] > K - A_sum[i]:
            j -= 1
        ans = max(ans, i + j)
    print(ans)

=======
Suggestion 6

def main():
    N,M,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    Asum = [0]
    Bsum = [0]
    for i in range(N):
        Asum.append(Asum[i]+A[i])
    for i in range(M):
        Bsum.append(Bsum[i]+B[i])
    ans = 0
    j = M
    for i in range(N+1):
        if Asum[i] > K:
            break
        while Bsum[j] > K-Asum[i]:
            j -= 1
        ans = max(ans,i+j)
    print(ans)

=======
Suggestion 7

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A_cumsum = [0] * (N + 1)
    B_cumsum = [0] * (M + 1)

    for i in range(N):
        A_cumsum[i + 1] = A_cumsum[i] + A[i]

    for i in range(M):
        B_cumsum[i + 1] = B_cumsum[i] + B[i]

    ans = 0
    for i in range(N + 1):
        if A_cumsum[i] > K:
            break

        ok = -1
        ng = M + 1

        while ng - ok > 1:
            mid = (ok + ng) // 2
            if A_cumsum[i] + B_cumsum[mid] <= K:
                ok = mid
            else:
                ng = mid

        ans = max(ans, i + ok)

    print(ans)

=======
Suggestion 8

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 累積和をとる
    for i in range(1, N):
        A[i] += A[i-1]
    for i in range(1, M):
        B[i] += B[i-1]

    # 二分探索
    ans = 0
    for i in range(N):
        if A[i] > K:
            break
        l = 0
        r = M
        while l < r:
            m = (l+r)//2
            if A[i] + B[m] <= K:
                l = m+1
            else:
                r = m
        ans = max(ans, i+1+l)
    for i in range(M):
        if B[i] > K:
            break
        l = 0
        r = N
        while l < r:
            m = (l+r)//2
            if B[i] + A[m] <= K:
                l = m+1
            else:
                r = m
        ans = max(ans, i+1+l)
    print(ans)

=======
Suggestion 9

def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # 累積和を取得
    a_sum = [0] * (n + 1)
    b_sum = [0] * (m + 1)
    for i in range(n):
        a_sum[i + 1] = a_sum[i] + a[i]
    for i in range(m):
        b_sum[i + 1] = b_sum[i] + b[i]

    ans = 0
    j = m
    for i in range(n + 1):
        if a_sum[i] > k:
            break
        while b_sum[j] > k - a_sum[i]:
            j -= 1
        ans = max(ans, i + j)
    print(ans)

=======
Suggestion 10

def solution():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    i = 0
    j = 0
    sum = 0
    while sum <= K and (i < N or j < M):
        if i < N and j < M:
            if A[i] < B[j]:
                i += 1
                sum += A[i-1]
            else:
                j += 1
                sum += B[j-1]
        elif i < N:
            i += 1
            sum += A[i-1]
        elif j < M:
            j += 1
            sum += B[j-1]
        if sum <= K:
            ans += 1
    print(ans)
solution()
