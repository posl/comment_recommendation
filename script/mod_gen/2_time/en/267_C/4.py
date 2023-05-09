def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # B = [0] * N
    # for i in range(N):
    #     B[i] = A[i]
    #     if i >= M:
    #         B[i] += B[i - M]
    # B.sort(reverse=True)
    # print(sum([i * B[i] for i in range(M)]))
    B = [0] * (N - M + 1)
    for i in range(N - M + 1):
        B[i] = sum(A[i:i + M])
    B.sort(reverse=True)
    print(sum([i * B[i] for i in range(M)]))

if __name__ == '__main__':
    main()