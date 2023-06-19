def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    B = []
    for i in range(N):
        B.append(A[i][0])
        B.append(A[i][0] + A[i][1])
    B.sort()
    C = []
    for i in range(2 * N - 1):
        C.append(B[i + 1] - B[i])
    D = [0] * N
    for i in range(2 * N - 1):
        if C[i] != 0:
            D[C[i] - 1] += 1
    for i in range(N):
        print(D[i], end = ' ')
