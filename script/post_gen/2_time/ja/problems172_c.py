Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A_sum = [0]
    B_sum = [0]
    for a in A:
        A_sum.append(A_sum[-1] + a)
    for b in B:
        B_sum.append(B_sum[-1] + b)
    ans = 0
    for i in range(N + 1):
        if A_sum[i] > K:
            break
        ans = max(ans, i + (M - (len(B_sum) - bisect.bisect_right(B_sum, K - A_sum[i]))) + 1)
    print(ans)

=======
Suggestion 2

def main():
    # 入力
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 累積和を求める
    A_sum = [0] * (N + 1)
    B_sum = [0] * (M + 1)
    for i in range(N):
        A_sum[i + 1] = A_sum[i] + A[i]
    for i in range(M):
        B_sum[i + 1] = B_sum[i] + B[i]

    # 二分探索
    ans = 0
    j = M
    for i in range(N + 1):
        if A_sum[i] > K:
            break
        while A_sum[i] + B_sum[j] > K:
            j -= 1
        ans = max(ans, i + j)

    # 出力
    print(ans)

=======
Suggestion 3

def main():
    # 入力
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 累積和
    for i in range(1, N):
        A[i] += A[i-1]
    for i in range(1, M):
        B[i] += B[i-1]
    # 二分探索
    ans = 0
    j = M
    for i in range(N+1):
        if i == N:
            t = K
        else:
            t = K - A[i]
        if t < 0:
            continue
        while j > 0 and B[j-1] > t:
            j -= 1
        ans = max(ans, i+j)
    # 出力
    print(ans)

=======
Suggestion 4

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A_sum = [0] * (N + 1)
    B_sum = [0] * (M + 1)
    for i in range(N):
        A_sum[i + 1] = A_sum[i] + A[i]
    for i in range(M):
        B_sum[i + 1] = B_sum[i] + B[i]

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
Suggestion 5

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    Asum = [0] * (N + 1)
    Bsum = [0] * (M + 1)

    for i in range(N):
        Asum[i + 1] = Asum[i] + A[i]
    for i in range(M):
        Bsum[i + 1] = Bsum[i] + B[i]

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
Suggestion 6

def main():
    #入力
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    #累積和
    A_sum = [0] * (N + 1)
    B_sum = [0] * (M + 1)
    for i in range(N):
        A_sum[i + 1] = A_sum[i] + A[i]
    for i in range(M):
        B_sum[i + 1] = B_sum[i] + B[i]
    #本の数を数える
    ans = 0
    for i in range(N + 1):
        if A_sum[i] > K:
            break
        j = M
        while B_sum[j] > K - A_sum[i]:
            j -= 1
        ans = max(ans, i + j)
    #出力
    print(ans)

=======
Suggestion 7

def main():
    # input
    N, M, K = map(int, input().split())
    As = list(map(int, input().split()))
    Bs = list(map(int, input().split()))

    # compute
    # 机 A に積まれている本の累積和を計算
    As = [0] + list(accumulate(As))
    # 机 B に積まれている本の累積和を計算
    Bs = [0] + list(accumulate(Bs))
    # 机 A に積まれている本の数を計算
    n = bisect.bisect_right(As, K)
    # 机 B に積まれている本の数を計算
    m = bisect.bisect_right(Bs, K)
    # 机 A に積まれている本の数を減らしながら、机 B に積まれている本の数を増やす
    for i in range(n):
        j = bisect.bisect_right(Bs, K-As[i])
        m = max(m, i+j)

    # output
    print(m)

=======
Suggestion 8

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 机Aの本を読むのにかかる時間の累積和
    A_sum = [0]
    for a in A:
        A_sum.append(A_sum[-1] + a)
    # 机Bの本を読むのにかかる時間の累積和
    B_sum = [0]
    for b in B:
        B_sum.append(B_sum[-1] + b)
    # 机Aの本を読むのにかかる時間の累積和がKを超える最小のindex
    A_index = 0
    # 机Bの本を読むのにかかる時間の累積和がKを超える最小のindex
    B_index = 0
    # 机Aの本を読むのにかかる時間の累積和がKを超える最小のindexを求める
    while A_index < N + 1:
        if A_sum[A_index] > K:
            break
        A_index += 1
    # 机Bの本を読むのにかかる時間の累積和がKを超える最小のindexを求める
    while B_index < M + 1:
        if B_sum[B_index] > K:
            break
        B_index += 1
    # 机Aの本を読むのにかかる時間の累積和がKを超える最小のindexを1減らす
    A_index -= 1
    # 机Bの本を読むのにかかる時間の累積和がKを超える最小のindexを1減らす
    B_index -= 1
    # 机Aの本を読むのにかかる時間の累積和がKを超える最小のindexと机Bの本を読むのにかかる時間の累

=======
Suggestion 9

def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # 机Aの本を読むのにかかる時間の累積和
    a_sum = [0]
    for i in a:
        a_sum.append(a_sum[-1] + i)

    # 机Bの本を読むのにかかる時間の累積和
    b_sum = [0]
    for i in b:
        b_sum.append(b_sum[-1] + i)

    # 机Aの本を読むのにかかる時間の累積和のうち、k分以内に読むことができる本の最大数
    max_a = 0
    for i in range(n+1):
        if a_sum[i] > k:
            break
        max_a = i

    # 机Bの本を読むのにかかる時間の累積和のうち、k分以内に読むことができる本の最大数
    max_b = 0
    for i in range(m+1):
        if b_sum[i] > k:
            break
        max_b = i

    # 机Aの本を読むのにかかる時間の累積和のうち、k分以内に読むことができる本の最大数と、
    # 机Bの本を読むのにかかる時間の累積和のうち、k分以内に読むことができる本の最大数の合計が最大となるものを探索する
    ans = 0
    for i in range(max_a+1):
        for j in range(max_b+1):
            if a_sum[i] + b_sum[j] <= k:
                ans = max(ans, i + j)

    print(ans)

=======
Suggestion 10

def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # 机Aの読むのに要する時間の累積和
    a_sum = [0] * (n + 1)
    for i in range(n):
        a_sum[i + 1] = a_sum[i] + a[i]

    # 机Bの読むのに要する時間の累積和
    b_sum = [0] * (m + 1)
    for i in range(m):
        b_sum[i + 1] = b_sum[i] + b[i]

    # 机Aの読むのに要する時間の累積和をk以下になるまで減らす
    ans = 0
    j = m
    for i in range(n + 1):
        if a_sum[i] > k:
            break
        while b_sum[j] > k - a_sum[i]:
            j -= 1
        ans = max(ans, i + j)

    print(ans)
