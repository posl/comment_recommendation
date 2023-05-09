def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] >= 0:
        print(A[K - 1])
        return
    if A[-1] <= 0:
        if K % 2 == 0:
            print(-A[N - K])
        else:
            print(A[N - K])
        return
    if K == (N * (N - 1)) // 2:
        print(A[-1] * A[-2])
        return
    i = 0
    j = N - 1
    while i < j:
        if A[i] * A[j] <= 0:
            break
        if A[i] * A[j] < A[i + 1] * A[j - 1]:
            i += 1
        else:
            j -= 1
    if K <= i * (N - j):
        print(A[i] * A[i + K // (N - j)])
        return
    K -= i * (N - j)
    print(A[j - K // (i + 1)] * A[j])
