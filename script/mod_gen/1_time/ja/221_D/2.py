def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    D = [0] * N
    for i in range(N):
        D[0] += B[i] - 1
        D[i] += 1
        if i < N - 1:
            D[i + 1] += A[i + 1] - (A[i] + B[i]) - 1
    print(*D, sep=" ")

if __name__ == '__main__':
    main()