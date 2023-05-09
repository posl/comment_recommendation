def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = [0] * (N + 1)
    for i in range(N):
        B[i + 1] = B[i] + A[i]
    for i in range(N):
        if i == N - 1:
            print(K)
        else:
            if (A[i + 1] - 1) * (i + 1) <= K:
                K -= (A[i + 1] - 1) * (i + 1)
            else:
                print(K // (i + 1) + B[i])
                K = 0

if __name__ == '__main__':
    main()