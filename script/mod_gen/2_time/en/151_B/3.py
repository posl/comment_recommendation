def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    total = sum(A)
    if total / N >= M:
        print(0)
        return
    if (N-1) * K - total < M - total / N:
        print(-1)
        return
    print(M * N - total)

if __name__ == '__main__':
    main()