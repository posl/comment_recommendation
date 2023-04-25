Synthesizing 10/10 solutions

=======
Suggestion 1

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
Suggestion 2

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
    for i in range(N+1):
        if A_sum[i] > K:
            break
        tmp = i
        tmp += (M - (len(B_sum) - 1 - B_sum[::-1].index(bisect.bisect_right(B_sum, K - A_sum[i]) - 1)))
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 3

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
    for i in range(N + 1):
        if A_sum[i] > K:
            break
        ans = max(ans, i + (M - (B_sum[bisect.bisect_right(B_sum, K - A_sum[i]) - 1] > K)))
    print(ans)

=======
Suggestion 4

def main():
    N, M, K = map(int, input().split())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    A = [0] + A
    B = [0] + B
    for i in range(N):
        A[i+1] += A[i]
    for i in range(M):
        B[i+1] += B[i]
    ans = 0
    j = M
    for i in range(N+1):
        if A[i] > K:
            break
        while B[j] > K - A[i]:
            j -= 1
        ans = max(ans, i + j)
    print(ans)

=======
Suggestion 5

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    a, b, ans = 0, 0, 0
    while a < N and A[a] <= K:
        K -= A[a]
        a += 1
    ans = a
    for i in range(M):
        if K < B[i]:
            break
        K -= B[i]
        b += 1
        while a > 0 and K < A[a - 1]:
            K += A[a - 1]
            a -= 1
        ans = max(ans, a + b)
    print(ans)

=======
Suggestion 6

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # Aの累積和を求める
    A_sum = [0] * (N + 1)
    for i in range(N):
        A_sum[i + 1] = A_sum[i] + A[i]

    # Bの累積和を求める
    B_sum = [0] * (M + 1)
    for i in range(M):
        B_sum[i + 1] = B_sum[i] + B[i]

    # Bの累積和をK以下になるようにする
    B_sum = [x for x in B_sum if x <= K]

    # Aの累積和をK以下になるようにする
    # そのときのBの累積和の最大値を求める
    ans = 0
    for i in range(N + 1):
        if A_sum[i] > K:
            break
        j = bisect.bisect_right(B_sum, K - A_sum[i])
        ans = max(ans, i + j)

    print(ans)

=======
Suggestion 7

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # Aの累積和
    Asum = [0]
    for i in range(N):
        Asum.append(A[i] + Asum[i])

    # Bの累積和
    Bsum = [0]
    for i in range(M):
        Bsum.append(B[i] + Bsum[i])

    # Aの累積和 + Bの累積和
    Csum = [0]
    for i in range(M):
        Csum.append(Bsum[i] + Asum[-1])

    # Bの累積和 + Aの累積和
    Dsum = [0]
    for i in range(N):
        Dsum.append(Asum[i] + Bsum[-1])

    # Aの累積和 + Bの累積和 と Bの累積和 + Aの累積和 のうち、K以下の最大値を求める
    ans = 0
    for i in range(N+1):
        if Asum[i] > K:
            break
        ans = max(ans, i + bisect.bisect_right(Csum, K-Asum[i])-1)
    for i in range(M+1):
        if Bsum[i] > K:
            break
        ans = max(ans, i + bisect.bisect_right(Dsum, K-Bsum[i])-1)

    print(ans)

=======
Suggestion 8

def main():
    # Read input
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # Calculate cumulative sum of A and B
    A_sum = [0] * (N + 1)
    B_sum = [0] * (M + 1)
    for i in range(N):
        A_sum[i + 1] = A_sum[i] + A[i]
    for i in range(M):
        B_sum[i + 1] = B_sum[i] + B[i]
    # Calculate the maximum number of books that can be read
    max_num = 0
    j = M
    for i in range(N + 1):
        if A_sum[i] > K:
            break
        while B_sum[j] > K - A_sum[i]:
            j -= 1
        max_num = max(max_num, i + j)
    # Output the answer
    print(max_num)

=======
Suggestion 9

def main():
    #Read Input
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    #A = [60, 90, 120]
    #B = [80, 150, 80, 150]
    #N = 3
    #M = 4
    #K = 240
    #A = [60, 90, 120]
    #B = [80, 150, 80, 150]
    #N = 3
    #M = 4
    #K = 730
    #A = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]
    #B = [1000000000, 1000000000, 1000000000, 1000000000]
    #N = 5
    #M = 4
    #K = 1
    #A = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]
    #B = [1000000000, 1000000000, 1000000000, 1000000000]
    #N = 5
    #M = 4
    #K = 10000000000
    #A = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]
    #B = [1000000000, 1000000000, 1000000000, 1000000000]
    #N = 5
    #M = 4
    #K = 1000000000000000000
    #A = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]
    #B = [1000000000, 1000000000, 1000000000, 1000000000]
    #N = 5
    #M = 4
    #K = 10000000000000000000
    #A = [1000000000,

=======
Suggestion 10

def read_ints():
    return list(map(int, input().split()))
