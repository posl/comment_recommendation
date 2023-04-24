Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M, K = map(int, input().split())
    A = [0] + list(map(int, input().split()))
    B = [0] + list(map(int, input().split()))
    for i in range(1, N+1):
        A[i] = A[i-1] + A[i]
    for i in range(1, M+1):
        B[i] = B[i-1] + B[i]
    ans = 0
    j = M
    for i in range(N+1):
        if A[i] > K:
            break
        while B[j] > K - A[i]:
            j -= 1
        ans = max(ans, i+j)
    print(ans)
main()

=======
Suggestion 2

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.insert(0, 0)
    B.insert(0, 0)
    for i in range(1, N+1):
        A[i] += A[i-1]
    for i in range(1, M+1):
        B[i] += B[i-1]
    ans = 0
    j = M
    for i in range(N+1):
        if A[i] > K:
            break
        while B[j] > K - A[i]:
            j -= 1
        ans = max(ans, i+j)
    print(ans)

=======
Suggestion 3

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    a = [0]
    b = [0]
    for i in range(N):
        a.append(a[i] + A[i])
    for i in range(M):
        b.append(b[i] + B[i])
    ans = 0
    j = M
    for i in range(N + 1):
        if a[i] > K:
            break
        while b[j] > K - a[i]:
            j -= 1
        ans = max(ans, i + j)
    print(ans)

=======
Suggestion 4

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    Asum = [0]
    Bsum = [0]
    for a in A:
        Asum.append(Asum[-1] + a)
    for b in B:
        Bsum.append(Bsum[-1] + b)
    ans = 0
    j = M
    for i in range(N + 1):
        if Asum[i] > K:
            break
        while Bsum[j] > K - Asum[i]:
            j -= 1
        ans = max(ans, i + j)
    print(ans)

=======
Suggestion 5

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    Asum = [0]
    Bsum = [0]
    for i in range(N):
        Asum.append(Asum[-1]+A[i])
    for i in range(M):
        Bsum.append(Bsum[-1]+B[i])
    ans = 0
    j = M
    for i in range(N+1):
        if Asum[i] > K:
            break
        while Bsum[j] > K-Asum[i]:
            j -= 1
        ans = max(ans, i+j)
    print(ans)

=======
Suggestion 6

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
    for i in range(N + 1):
        if A_sum[i] > K:
            break
        while B_sum[j] > K - A_sum[i]:
            j -= 1
        ans = max(ans, i + j)
    print(ans)

=======
Suggestion 7

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for i in range(N + 1):
        if i == 0:
            a = 0
        else:
            a = A[i - 1]
        if K - a < 0:
            break
        cnt = i
        k = K - a
        for j in range(M + 1):
            if j == 0:
                b = 0
            else:
                b = B[j - 1]
            if k - b < 0:
                break
            cnt += 1
            k -= b
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 8

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    Asum = [0] * (N+1)
    Bsum = [0] * (M+1)
    for i in range(N):
        Asum[i+1] = Asum[i] + A[i]
    for i in range(M):
        Bsum[i+1] = Bsum[i] + B[i]

    ans = 0
    for i in range(N+1):
        if Asum[i] > K:
            break
        j = M
        while Asum[i] + Bsum[j] > K:
            j -= 1
        ans = max(ans, i + j)

    print(ans)

=======
Suggestion 9

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # create cumulative sums of list A and B
    A_cumsum = [0] + list(accumulate(A))
    B_cumsum = [0] + list(accumulate(B))
    # find the max number of books that can be read in K minutes
    ans = 0
    for i in range(N + 1):
        if A_cumsum[i] > K:
            break
        # binary search for the largest j that satisfies B_cumsum[j] <= K - A_cumsum[i]
        j = bisect.bisect_right(B_cumsum, K - A_cumsum[i])
        ans = max(ans, i + j - 1)
    print(ans)
