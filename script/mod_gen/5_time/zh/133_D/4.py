def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [0] * N
    for i in range(N):
        if i % 2 == 0:
            B[0] += A[i]
        else:
            B[0] -= A[i]
    B[0] //= 2
    for i in range(1, N):
        B[i] = A[i - 1] - B[i - 1]
    for i in range(N):
        if i == N - 1:
            print(B[i])
        else:
            print(B[i], end=' ')

if __name__ == '__main__':
    main()