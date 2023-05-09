def main():
    # N P Q R S
    # A_1 A_2 ... A_N
    N, P, Q, R, S = map(int, input().split())
    A = list(map(int, input().split()))
    # A_1 A_2 ... A_P-1 A_P A_P+1 ... A_Q-1 A_Q A_Q+1 ... A_R-1 A_R A_R+1 ... A_S-1 A_S A_S+1 ... A_N
    # B_1 B_2 ... B_P-1 B_P B_P+1 ... B_Q-1 B_Q B_Q+1 ... B_R-1 B_R B_R+1 ... B_S-1 B_S B_S+1 ... B_N
    # B_1 B_2 ... B_R-1 B_R B_R+1 ... B_S-1 B_S B_S+1 ... B_Q-1 B_Q B_Q+1 ... B_P-1 B_P B_P+1 ... B_N
    B = A[:P-1] + A[R-1:S] + A[Q-1:R-1] + A[P-1:Q-1] + A[S:]
    print(*B)

if __name__ == '__main__':
    main()