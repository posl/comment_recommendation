def main():
    N, P, Q, R, S = map(int, input().split())
    A = list(map(int, input().split()))
    B = A[:P-1] + A[R-1:S] + A[Q-1:R-1] + A[P-1:Q-1] + A[S:]
    print(*B)

if __name__ == '__main__':
    main()