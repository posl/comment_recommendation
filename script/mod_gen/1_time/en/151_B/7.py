def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    A_sum = sum(A)
    if A_sum + K * N >= M * N:
        print(max(M * N - A_sum, 0))
    else:
        print(-1)

if __name__ == '__main__':
    main()