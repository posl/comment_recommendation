def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        if i % 2 == 0:
            B[0] += A[i]
        else:
            B[0] -= A[i]
    for i in range(1, N):
        B[i] = 2 * A[i - 1] - B[i - 1]
    print(*B)

if __name__ == '__main__':
    main()