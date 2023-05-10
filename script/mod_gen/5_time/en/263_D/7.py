def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    S = sum(A)
    min_sum = S
    for i in range(N):
        for j in range(N - i):
            S = S - A[i + j]
            S = S + (i + j) * L + (N - 1 - i - j) * R
            if min_sum > S:
                min_sum = S
            S = S + A[i + j]
            S = S - (i + j) * L - (N - 1 - i - j) * R
    print(min_sum)

if __name__ == '__main__':
    main()