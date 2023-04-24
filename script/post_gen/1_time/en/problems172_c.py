Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, K = map(int, input().split())
    A = [0] + list(map(int, input().split()))
    B = [0] + list(map(int, input().split()))

    for i in range(1, N + 1):
        A[i] += A[i - 1]
    for i in range(1, M + 1):
        B[i] += B[i - 1]

    ans = 0
    j = M
    for i in range(N + 1):
        if A[i] > K:
            break
        while B[j] > K - A[i]:
            j -= 1
        ans = max(ans, i + j)
    print(ans)

=======
Suggestion 2

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    for i in range(1, N):
        A[i] += A[i - 1]
    for i in range(1, M):
        B[i] += B[i - 1]

    ans = 0
    j = M
    for i in range(-1, N):
        if i == -1:
            a = 0
        else:
            a = A[i]
        if a > K:
            break
        while B[j - 1] > K - a:
            j -= 1
            if j == 0:
                break
        ans = max(ans, i + j)
    print(ans)

=======
Suggestion 3

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.insert(0, 0)
    B.insert(0, 0)
    for i in range(1, N + 1):
        A[i] += A[i - 1]
    for i in range(1, M + 1):
        B[i] += B[i - 1]
    ans = 0
    j = M
    for i in range(N + 1):
        if A[i] > K:
            break
        while B[j] > K - A[i]:
            j -= 1
        ans = max(ans, i + j)
    print(ans)

=======
Suggestion 4

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    Asum = [0] * (N + 1)
    Bsum = [0] * (M + 1)
    for i in range(N):
        Asum[i + 1] = Asum[i] + A[i]
    for j in range(M):
        Bsum[j + 1] = Bsum[j] + B[j]
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
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

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
Suggestion 6

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    i = 0
    j = 0
    time = 0
    while i < N and time + A[i] <= K:
        time += A[i]
        i += 1
    ans = i
    while j < M and i >= 0:
        time += B[j]
        j += 1
        while time > K and i > 0:
            i -= 1
            time -= A[i]
        if time <= K:
            ans = max(ans, i + j)
    print(ans)

=======
Suggestion 7

def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.insert(0, 0)
    b.insert(0, 0)

    for i in range(1, n+1):
        a[i] += a[i-1]

    for i in range(1, m+1):
        b[i] += b[i-1]

    ans = 0
    j = m
    for i in range(n+1):
        if a[i] > k:
            break
        while b[j] > k - a[i]:
            j -= 1
        ans = max(ans, i + j)

    print(ans)

=======
Suggestion 8

def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_cum = [0] * (n + 1)
    b_cum = [0] * (m + 1)
    for i in range(n):
        a_cum[i + 1] = a_cum[i] + a[i]
    for i in range(m):
        b_cum[i + 1] = b_cum[i] + b[i]
    ans = 0
    for i in range(n + 1):
        if a_cum[i] > k:
            break
        j = bisect.bisect_right(b_cum, k - a_cum[i])
        ans = max(ans, i + j - 1)
    print(ans)

=======
Suggestion 9

def main():
    #入力
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    #累積和
    A_cumsum = [0]
    B_cumsum = [0]
    for i in range(N):
        A_cumsum.append(A_cumsum[i]+A[i])
    for i in range(M):
        B_cumsum.append(B_cumsum[i]+B[i])
    #Bの累積和がKを超える場所を探す
    B_cumsum = [i for i in B_cumsum if i <= K]
    #Aの累積和がKを超える場所を探す
    ans = 0
    for i in range(N+1):
        if A_cumsum[i] > K:
            break
        #Bの累積和がKを超える場所を探す
        j = binary_search(B_cumsum, K-A_cumsum[i])
        ans = max(ans, i+j)
    print(ans)

=======
Suggestion 10

def solve(N, M, K, A, B):
    # write your code here
    # return your answer
    return 0

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(solve(N, M, K, A, B))
