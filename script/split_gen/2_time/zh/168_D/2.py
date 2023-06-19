def main():
    N, M = map(int, input().split())
    A = [0 for _ in range(M)]
    B = [0 for _ in range(M)]
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    print(N, M, A, B)
