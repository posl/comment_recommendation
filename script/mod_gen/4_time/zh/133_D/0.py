def main():
    # N = int(input())
    # A = list(map(int, input().split()))
    N = 5
    A = [3, 8, 7, 5, 5]
    # N = 3
    # A = [1000000000, 1000000000, 0]
    B = [0] * N
    for i in range(N):
        if i % 2 == 0:
            B[0] += A[i]
        else:
            B[0] -= A[i]
    B[0] //= 2
    for i in range(N - 1):
        B[i + 1] = A[i] - B[i]
    for i in range(N):
        print(B[i], end=' ')

if __name__ == '__main__':
    main()