def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    for i in range(1, N + 1):
        print(len([j for j in range(M) if A[j] == i or B[j] == i]))
