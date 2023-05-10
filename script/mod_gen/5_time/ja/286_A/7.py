def main():
    N, P, Q, R, S = map(int, input().split())
    A = list(map(int, input().split()))
    B = A[P-1:Q] + A[R-1:S]
    A[P-1:Q] = B[R-P:S-P]
    A[R-1:S] = B[0:Q-P] + B[Q-P:]
    print(*A)

if __name__ == '__main__':
    main()