def main():
    N, P, Q, R, S = map(int, input().split())
    A = list(map(int, input().split()))
    B = A[:P-1] + A[Q:R-1] + A[S:]
    print(*B)

if __name__ == '__main__':
    main()