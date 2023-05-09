def main():
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    BC = [list(map(int,input().split())) for _ in range(Q)]
    B = [BC[i][0] for i in range(Q)]
    C = [BC[i][1] for i in range(Q)]
    S = [0 for _ in range(Q)]
    #print(N,A,Q,B,C,S)
    for i in range(Q):
        S[i] = sum(A)
        for j in range(N):
            if A[j] == B[i]:
                A[j] = C[i]
                S[i] = S[i] - B[i] + C[i]
        print(S[i])
    return

if __name__ == '__main__':
    main()