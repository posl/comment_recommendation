def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [-A[i] if i % 2 == 0 else A[i] for i in range(N)]
    print(sum(A) - sum(A[:N // 2]) * (L - R) + R * N // 2 - L * (N - N // 2))

if __name__ == '__main__':
    main()