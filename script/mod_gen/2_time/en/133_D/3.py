def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    C = [0] * N
    for i in range(N):
        B[i] = A[i] - A[(i + 1) % N]
    for i in range(N):
        C[i] = B[(i - 1) % N] + B[i]
    for i in range(N):
        print(C[i] // 2, end=' ')

if __name__ == '__main__':
    main()