Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A = [0] + A
    B = [0] + B

    for i in range(1, N+1):
        A[i] += A[i-1]
    for i in range(1, M+1):
        B[i] += B[i-1]

    max_books = 0
    j = M
    for i in range(N+1):
        if A[i] > K:
            break
        while B[j] > K - A[i]:
            j -= 1
        max_books = max(max_books, i + j)

    print(max_books)

=======
Suggestion 2

def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a = [0] + a
    b = [0] + b

    for i in range(n):
        a[i + 1] += a[i]
    for i in range(m):
        b[i + 1] += b[i]

    ans = 0
    j = m
    for i in range(n + 1):
        if a[i] > k:
            break
        while b[j] > k - a[i]:
            j -= 1
        ans = max(ans, i + j)

    print(ans)

=======
Suggestion 3

def solve():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(1, n):
        a[i] += a[i - 1]
    for i in range(1, m):
        b[i] += b[i - 1]
    result = 0
    for i in range(n):
        if a[i] > k:
            break
        result = i + 1
    for i in range(m):
        if b[i] > k:
            break
        result = max(result, i + 1)
    for i in range(n):
        if a[i] > k:
            break
        j = m - 1
        while j >= 0 and a[i] + b[j] > k:
            j -= 1
        result = max(result, i + 1 + j + 1)
    for i in range(m):
        if b[i] > k:
            break
        j = n - 1
        while j >= 0 and b[i] + a[j] > k:
            j -= 1
        result = max(result, i + 1 + j + 1)
    print(result)

=======
Suggestion 4

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
        while a_sum[i] + b_sum[j] > k:
            j -= 1
        ans = max(ans, i + j)

    print(ans)

=======
Suggestion 5

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
Suggestion 6

def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a_sum = [0]
    for i in range(n):
        a_sum.append(a_sum[i] + a[i])

    b_sum = [0]
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
Suggestion 7

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 累積和
    for i in range(1, N):
        A[i] += A[i-1]
    for i in range(1, M):
        B[i] += B[i-1]

    # 答え
    ans = 0

    # A から i 冊読む
    for i in range(N+1):
        # A から i 冊読むのにかかる時間
        a = A[i-1] if i > 0 else 0
        # A から i 冊読んで残りの時間で B から読める冊数
        b = 0 if K < a else len(B) - bisect.bisect_right(B, K - a)
        ans = max(ans, i + b)

    print(ans)

=======
Suggestion 8

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 累積和を求める
    A_sum = [0] * (N + 1)
    for i in range(N):
        A_sum[i + 1] = A_sum[i] + A[i]

    B_sum = [0] * (M + 1)
    for i in range(M):
        B_sum[i + 1] = B_sum[i] + B[i]

    # 累積和のうち、K以下で最大のものを探す
    ans = 0
    j = M
    for i in range(N + 1):
        if A_sum[i] > K:
            break
        while B_sum[j] > K - A_sum[i]:
            j -= 1
        ans = max(ans, i + j)

    print(ans)

main()

=======
Suggestion 9

def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    #累積和を計算
    a_sum = [0] * (n+1)
    for i in range(n):
        a_sum[i+1] = a_sum[i] + a[i]
    b_sum = [0] * (m+1)
    for i in range(m):
        b_sum[i+1] = b_sum[i] + b[i]

    #累積和の中から、kを超えない最大値を求める
    ans = 0
    b_index = m
    for i in range(n+1):
        if a_sum[i] > k:
            break
        while b_sum[b_index] > k - a_sum[i]:
            b_index -= 1
        ans = max(ans, i + b_index)
    print(ans)

=======
Suggestion 10

def get_max_books(n, m, k, a, b):
    if n == 0 or m == 0:
        return 0
    if a[0] > k and b[0] > k:
        return 0
    if a[0] > k:
        return get_max_books(n, m-1, k, a, b[1:])
    if b[0] > k:
        return get_max_books(n-1, m, k, a[1:], b)
    return 1 + max(get_max_books(n, m-1, k-b[0], a, b[1:]), get_max_books(n-1, m, k-a[0], a[1:], b))
