def main():
    N = int(input())
    S = list(input())
    Q = int(input())
    T = [0] * Q
    A = [0] * Q
    B = [0] * Q
    for i in range(Q):
        T[i], A[i], B[i] = map(int, input().split())
    #print("N=", N)
    #print("S=", S)
    #print("Q=", Q)
    #print("T=", T)
    #print("A=", A)
    #print("B=", B)
    #print("".join(S))
    for i in range(Q):
        if T[i] == 1:
            S[A[i]-1], S[B[i]-1] = S[B[i]-1], S[A[i]-1]
        elif T[i] == 2:
            S[0:N], S[N:2*N] = S[N:2*N], S[0:N]
        #print("".join(S))
    print("".join(S))

if __name__ == '__main__':
    main()