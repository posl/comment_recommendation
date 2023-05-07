def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    print(N - 1)
    for i in range(1, M):
        if A[i] < B[i]:
            print((A[i] - 1) * (N - B[i]))
        else:
            print((B[i] - 1) * (N - A[i]))
