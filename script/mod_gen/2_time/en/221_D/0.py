def main():
    N = int(input())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    D = [0] * (N + 1)
    for i in range(N):
        D[A[i]] += 1
        D[A[i] + B[i]] -= 1
    for i in range(1, N + 1):
        D[i] += D[i - 1]
    for i in range(1, N + 1):
        D[i] = D[i - 1] + D[i]
    for i in range(1, N + 1):
        print(D[i] - D[i - 1], end = ' ')
    print()

if __name__ == '__main__':
    main()