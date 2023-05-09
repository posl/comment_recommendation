def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    A.sort()
    A = A[1:]
    B = [0] * (N + 1)
    C = [0] * (N + 1)
    for i in range(N):
        if A[i] == A[i + 1]:
            B[i + 1] = B[i] + 1
        else:
            B[i + 1] = B[i]
    for i in range(N - 1, -1, -1):
        if A[i] == A[i + 1]:
            C[i] = C[i + 1] + 1
        else:
            C[i] = C[i + 1]
    for i in range(N):
        print(N - B[i + 1] - C[i] - 1)
main()
