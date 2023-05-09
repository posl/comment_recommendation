def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    for i in range(N - 1, -1, -1):
        B[i] = B[i + 1] + A[i]
    C = [0] * (N + 1)
    for i in range(N - 1, -1, -1):
        C[i] = C[i + 1]
        if i + 1 < N and A[i] == A[i + 1]:
            C[i] += 1
    for i in range(N):
        if A[i] == 2:
            print(B[i + 1])
        else:
            print(B[i + 1] - C[i + 1])

if __name__ == '__main__':
    main()