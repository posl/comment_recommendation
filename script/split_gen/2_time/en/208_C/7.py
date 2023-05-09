def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A
    for i in range(N):
        if K <= (A[i + 1] - A[i] - 1) * (i + 1):
            break
        else:
            K -= (A[i + 1] - A[i] - 1) * (i + 1)
    print(K // (i + 1) + A[i])
    for j in range(i + 1, N):
        print(K // (i + 1) + A[i] + K % (i + 1) - (j - i) * (A[j] - A[j - 1] - 1))
