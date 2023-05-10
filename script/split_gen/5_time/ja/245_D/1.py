def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0] * (M + 1)
    for i in range(N + 1):
        for j in range(M + 1):
            B[j] += A[i] * C[i + j]
    output = ""
    for i in range(M):
        output += str(B[i]) + " "
    output += str(B[M])
    print(output)
